import os
import logging
import click
from infra_terraform.terraform import Terraform

@click.group()
def cli():
    pass

@cli.command()
@click.option('--path', default='./', help='Path to Terraform configuration')
@click.option('--state', default='terraform.tfstate', help='Path to Terraform state file')
def init(path, state):
    """Initialize Terraform in the given directory"""
    terraform = Terraform(path, state)
    terraform.init()

@cli.command()
@click.option('--path', default='./', help='Path to Terraform configuration')
@click.option('--state', default='terraform.tfstate', help='Path to Terraform state file')
def apply(path, state):
    """Apply Terraform configuration"""
    terraform = Terraform(path, state)
    terraform.apply()

@cli.command()
@click.option('--path', default='./', help='Path to Terraform configuration')
@click.option('--state', default='terraform.tfstate', help='Path to Terraform state file')
def destroy(path, state):
    """Destroy Terraform configuration"""
    terraform = Terraform(path, state)
    terraform.destroy()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    cli()