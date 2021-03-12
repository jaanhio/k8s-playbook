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

# Problems encountered

### Using community.kubernetes.k8s
Under the hood, this ansible plugin uses `kubernetes` and `openshift` python modules.

After some google-fu, realized its due to multiple related issues:
1. outdated version of python3.5 running on machine
2. outdated version of pip
3. above issues resulted in error installing `kubernetes` and `openshift` modules

### Steps
Install `software-properties-common`
```
apt-get install -y software-properties-common
```

Add apt-repository
```
add-apt-repository ppa:deadsnakes/ppa
```

Install `python3.9`
```
apt-get install -y python3.9
```

Install `distutils`.
```
apt-get install python3.9-distutils 
```

Install `pip`.
```
wget https://bootstrap.pypa.io/get-pip.py
/usr/bin/python3.9 get-pip.py
```

Install `kubernetes` and `openshift`.
```
/usr/bin/python3.9 -m pip install kubernetes openshift
```

### Additional changes required for setting up k8s on raspberry pi
Recent k8s setup on raspberry pi has been failing due to health check failure during the `kubeadm init` constrol plane bootup phase. 
```
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
I0311 15:10:40.823983   29341 round_trippers.go:425] curl -k -v -XGET  -H "Accept: application/json, */*" -H "User-Agent: kubeadm/v1.20.4 (linux/arm) kubernetes/e87da0b" 'https://192.168.1.221:6443/healthz?timeout=10s'
I0311 15:10:40.824625   29341 round_trippers.go:445] GET https://192.168.1.221:6443/healthz?timeout=10s  in 0 milliseconds
I0311 15:10:40.824699   29341 round_trippers.go:451] Response Headers:
```

It is likely due to lack of support for `cgroups` out of the box. Refer to this articles for possible solution https://opensource.com/article/20/6/kubernetes-raspberry-pi