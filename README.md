# snapshotalyzer-33000

Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance shapshots.

## Configuring

shotty uses the configuration file created by the AWS cli. e.g.
`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>`

*command*: instances/volumes/shapshots
*subcommand*: depends on command
*project* is optional
