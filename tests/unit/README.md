#!/usr/bin/env python3

"""
This is a Python script that uses the Terraform CLI to provision infrastructure.
"""

import subprocess
import os

def main():
    # Define the Terraform configuration file path
    config_file = 'infrastructure/main.tf'

    # Initialize Terraform
    subprocess.run(['terraform', 'init'])

    # Plan the infrastructure
    subprocess.run(['terraform', 'plan'])

    # Apply the changes to the infrastructure
    subprocess.run(['terraform', 'apply', '-auto-approve'])

if __name__ == '__main__':
    main()