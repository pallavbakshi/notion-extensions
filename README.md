# notion-extensions
Extending Notion's capabilities

In this project 'notion-extensions', I plan to build a few extensions to Notion's capabilities. I will be using the Notion API to build these extensions.

notion-extensions
    - notion-highlights

## Extension 1: Download all highlights from a Notion page

I'm calling the first extension notion-highlights. I'm building this because I want to be able to download all the highlights from a Notion page. I use Notion to take notes and I highlight the important parts of the notes. I want to be able to download all the highlights from a Notion page so that I can review them later.

### What am I trying to build at a high-level?
- A way to download all the highlights from a given Notion page.

### How will notion-highlights work?
1. User gives a page_id.
2. notion-highlights gets the page content using page_id from Notion API.
3. notion-highlights checks if any of the children blocks contain formatted text.
4. notion-highlights extracts the formatted text out -- both the formatting and the plain text.
5. notion-highlights also saves the URL of the block from which it extracted those.
6. notion-highlights prints out the text, or puts it in a CSV, or puts it in a PDF (without formatting) or puts it back to a Notion page.


