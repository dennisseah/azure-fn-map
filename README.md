# azure-fn-map
This is a simple example on how to expose _Azure Map API_ with _Azure Function_ in _Python_.

# 1. Setup

## Create Resource Group, Azure Map and Function App
When creating Function App, please have the followings 
1. Runtime stack = Python
1. Version=3.8 (or a version that matches your _Python_ version)

and add an Application Setting under Configuration Section
```
SUBSCRIPTION_ID=<the primary/secondary key of Azure map>
```


## git clone
```bash
git clone https://github.com/dennisseah/azure-fn-map.git
```

## Setup Python Virtual Environment & install Python packages
you use `python` (instead of `python3`) if you are not on _mac-osx_
```bash
cd azure-fn-map.git
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```

## Install Azure Functions Extension for VSCode

# 2. Development
open _vscode_ on the current git folder
```bash
code .
```
create a file, `local.settings.json`. The content of this file is
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "SUBSCRIPTION_ID": "<the primary/secondary key of Azure map>"
  }
}
```

I have my `.vscode/launch.json` like this
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Attach to Python Functions",
            "type": "python",
            "request": "attach",
            "port": 9091,
            "preLaunchTask": "func: host start"
        }
    ]
}
```

I have my `.vscode/settings.json` like this
```json
{
    "python.pythonPath": "venv/bin/python",
    "azureFunctions.deploySubpath": ".",
    "azureFunctions.scmDoBuildDuringDeployment": true,
    "azureFunctions.pythonVenv": "venv",
    "azureFunctions.projectLanguage": "Python",
    "azureFunctions.projectRuntime": "~3",
    "debug.internalConsoleOptions": "neverOpen"
}
```

I have my `.vscode/extensions.json` like this
```json
{
  "recommendations": [
    "ms-azuretools.vscode-azurefunctions",
    "ms-python.python"
  ]
}
```

## Debugging
Click on the Run Icon on the Left Icon Panel, and then click on the _Attach to Python Functions_ option.
Once the debugger is up, you can point your browser to
```
http://localhost:7071/api/AddressSearch
http://localhost:7071/api/ReverseGeo
```

## Deploying to Azure Function App.
Click on the Azure Icon on the Left Icon Panel, and then click _Deploy to Function App_ icon.
Select the subscription and function app accordingly. Once the deployment is done,
you can point your browser to
```
http://localhost:7071/api/AddressSearch
http://localhost:7071/api/ReverseGeo
```
