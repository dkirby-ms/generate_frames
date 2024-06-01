# build.ps1

$image_name = "generate_frames"
$tag = "latest"
$acr_login_server = "bunnyacr.azurecr.io"

docker build . -t $image_name
docker tag "$image_name`:$tag" "$acr_login_server/$image_name`:$tag"
docker push "$acr_login_server/$image_name`:$tag"

# Login to Azure with MSI
Connect-AzAccount -Identity # must be run as admin

# Retrieve the secret from Azure Key Vault
Install-Module Az.KeyVault
Import-Module Az.KeyVault
$keyVaultName = "kv-bunnyai"
$secretName = "ROBOFLOW-API-KEY"
$key = Get-AzKeyVaultSecret -VaultName $keyVaultName -Name $secretName -AsPlainText

docker run -e ROBOFLOW_API_KEY=$key -e FRAMES_PATH="c:\dev\cameras\bunnyai\images\" "$acr_login_server/$image_name`:$tag"
