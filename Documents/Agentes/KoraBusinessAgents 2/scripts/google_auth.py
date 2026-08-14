from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main() -> None:
    credentials_path = Path("credentials/google_credentials.json")
    token_path = Path("credentials/google_token.json")

    if not credentials_path.exists():
        raise FileNotFoundError(
            "No existe credentials/google_credentials.json. "
            "Descarga el OAuth Client JSON desde Google Cloud."
        )

    token_path.parent.mkdir(parents=True, exist_ok=True)

    flow = InstalledAppFlow.from_client_secrets_file(
        str(credentials_path),
        SCOPES,
    )

    creds = flow.run_local_server(port=0)

    with open(token_path, "w", encoding="utf-8") as token_file:
        token_file.write(creds.to_json())

    print(f"Token guardado en {token_path}")


if __name__ == "__main__":
    main()
