
from prefect import flow, task
import subprocess

@task
def git_status():
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(result.stdout)
    return result.returncode

@flow(name="hello-claw-flow")
def hello_claw_flow():
    code = git_status()
    if code == 0:
        print("✅ Git status ran successfully")
    else:
        print("❌ Git status failed")

if __name__ == "__main__":
    hello_claw_flow()
