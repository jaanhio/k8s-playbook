import sys

ansible_detected_machine_arch = sys.argv[1].lower()

def is_amd64(name):
    amd64_namings = ['x86_64', 'x64', 'x86-64', 'amd64', 'intel 64']
    return name in amd64_namings

def get_arm_version_number(name):
    return name[4]

def is_arm(name):
    return 'armv' in name

if is_amd64(ansible_detected_machine_arch):
    print('amd64')

if is_arm(ansible_detected_machine_arch):
    
    version_number = get_arm_version_number(ansible_detected_machine_arch)

    if int(version_number) <= 7:
        print('armhf')
    else:
        print('arm64')