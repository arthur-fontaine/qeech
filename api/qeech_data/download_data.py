import os

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))


def download_data():
    download_dataset("shuyangli94/food-com-recipes-and-user-interactions")


def download_dataset(dataset_name: str):
    import kaggle

    kaggle.api.authenticate()

    kaggle.api.dataset_download_files(
        dataset_name,
        path=os.path.join(os.path.dirname(__file__), "..", "data"),
        unzip=True,
    )


if __name__ == "__main__":
    download_data()
