resource "azurerm_container_registry" "registry" {
  location            = var.location
  name                = "${var.resource_group_name}aksterraform"
  resource_group_name = var.resource_group_name
  sku                 = "Basic"
  admin_enabled        = true

}

resource "docker_image" "backend" {
  name = "${var.resource_group_name}aksterraform.azurecr.io/backend"
  build {
    context = "../dev/"
    tag     = ["latest"]
  }
}

resource "null_resource" "docker_push" {
      depends_on = [docker_image.backend, azurerm_kubernetes_cluster.default]
      provisioner "local-exec" {
      command = <<-EOT
        # Log in your Azure Container Registry 
        az acr login -n ${azurerm_container_registry.registry.name} 

        Push your docker image in the ACR registry 
        docker push ${docker_image.backend.name}

        Retrieve your AKS cluster credentials and set your computer to work in the context 
        of your AKS cluster
        az aks get-credentials --resource-group  ${var.resource_group_name} \
        --name  ${azurerm_kubernetes_cluster.default.name}

      EOT
      }
    }
