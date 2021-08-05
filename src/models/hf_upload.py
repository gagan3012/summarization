import shutil
from getpass import getpass
from pathlib import Path
import yaml

from model import Summarization
from huggingface_hub import HfApi, Repository


def upload(upload_model, model_name):
    hf_username = input("Enter your HuggingFace username:")
    hf_password = getpass("Enter your HuggingFace password:")
    if Path("./models").exists():
        shutil.rmtree("./models")
    token = HfApi().login(username=hf_username, password=hf_password)
    del hf_password
    model_url = HfApi().create_repo(token=token, name=model_name, exist_ok=True)
    model_repo = Repository(
        "./model",
        clone_from=model_url,
        use_auth_token=token,
        git_email=f"{hf_username}@users.noreply.huggingface.co",
        git_user=hf_username,
    )

    readme_txt = f"""
            ---
            Summarisation model {model_name}
            """.strip()

    (Path(model_repo.local_dir) / "README.md").write_text(readme_txt)
    upload_model.save_model()
    commit_url = model_repo.push_to_hub()

    print("Check out your model at:")
    print(commit_url)
    print(f"https://huggingface.co/{hf_username}/{model_name}")


if __name__ == "__main__":
    with open("model_params.yml") as f:
        params = yaml.safe_load(f)

    model = Summarization()
    model.load_model(model_dir="./models")

    upload(upload_model=model, model_name=params["name"])
