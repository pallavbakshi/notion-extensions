import os
import click
from pprint import pprint
from notion_client import Client

page_id = '2237cd4ccdb846999e9d1033d267cf3c'
block_id = 'fedeeafac48147889788347cc13fadb3'

# write click command line tool
# Write a click command to get input from the user

# Help me write a curl command to query the Notion API

# TODO: What if Notion changes schema?
# TODO: How to build this project into a package?
# TODO: How to write some tests?



@click.command()
@click.option('--block_id', type=str, help='block_id of Notion block or page.')
@click.option('--content', type=str, help='content you want to add to Notion block.')
def main(block_id, content):
    print("hello")

    token = ""

    notion = Client(auth=token)
    # list_users_response = notion.users.list()
    # pprint(list_users_response)

    # Retrieve a page
    # https://developers.notion.com/reference/get-page
    data = notion.pages.retrieve('f44e90a258784703bff147bc5631360e')
    pprint(type(data))
    pprint(data)

    # Retrieve comments for a block
    # https://developers.notion.com/reference/get-block-comments
    # data = notion.comments.list(block_id=block_id)
    # pprint(data)

    # Retrieve a block
    # https://developers.notion.com/reference/retrieve-a-block
    # content = notion.blocks.retrieve(block_id=block_id)
    # pprint(content)


if __name__ == '__main__':
    main()






