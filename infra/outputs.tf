output "kubernetes_cluster_name" {
  value = azurerm_kubernetes_cluster.default.name
}

output "resource_group_name" {
  value = var.resource_group_name
}


output "acr_registry_name" {
  value = azurerm_container_registry.registry.name
}