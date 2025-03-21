agent_name="Alex"
secret_message="Meet me at the park"
print(f"Original message: {secret_message}")
secret_message.isupper()
count=len(secret_message)
code="007"
print(f"Coded message: {count}#{secret_message.replace(' ','#')}{code}{agent_name}")
