# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "bas/contrib-stretch64"
  config.vm.box_version = "9.0.0"
  config.vm.network "private_network", ip: "192.168.50.50"
  config.vm.synced_folder "./frontend", "/var/project-aclu/frontend"
  config.vm.synced_folder "./backend", "/var/project-aclu/backend"
  config.vm.define "aclu" do |aclu|
  end
  config.vm.provision "shell", path: "provision-debian.sh", privileged: false
end
