# Raise your Own Errors

def brew_chai(flavor):
    if flavor not in ["masala","ginger","elaichi"]:
        raise ValueError("Unsupported Chai...")
    print(f"brewing {flavor} chai....")
    
brew_chai("mint")