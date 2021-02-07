# Introduction

This is an Ansible playbook for setting up k8s using `kubeadm` on Ubuntu & Debian servers.

Please make sure you have Ansible installed.

---

# How to use


### 1. Set up `inventory` file.

This inventory contains information on the target servers. You can refer to the existing `inventory` file for reference.

### 2. Specify custom setup variables in `/vars/users_vars.yaml`

You can specify the following:
* whether pods should be deployed on master node via `allow_deploy_on_master`
* network plugin to use. currently only supports `weave` and `flannel`
* `pod_network_cidr`
* any extra packages you may need on server via `extra_packages`
```
extra_packages:
  - nmap
  - traceroute
```

### 3. Run playbook
```
ansible-playbook -i inventory main.yaml
```

### 4. Have fun with your cluster!

---
