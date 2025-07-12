from dotenv import load_dotenv

DEVELOPMENT = False

def load_service_env(service_name=Path.cwd().name):
    load_dotenv()

    DEVELOPMENT = pydantic.TypeAdapter(bool).validate_python(os.getenv(constants.DEBUG))
    env_path = en