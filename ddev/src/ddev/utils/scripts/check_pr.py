def changelog_entry_suffix(pr_number: int, pr_url: str) -> str:
    return f' ([#{pr_number}]({pr_url}))'


    import subprocess

                        f'end with a link to the associated PR:\n`{suffix}`',
def changelog_impl(*, ref: str, diff_file: str, pr_file: str) -> None:
    import json


        with open(pr_file, 'r', encoding='utf-8') as f:
            pr = json.loads(f.read())['pull_request']

        pr_number = pr['number']
        pr_url = pr['html_url']
        pr_labels = [label['name'] for label in pr['labels']]
        pr_number = 1
        pr_url = f'https://github.com/DataDog/integrations-core/pull/{pr_number}'
        pr_labels = []

    if 'changelog/no-changelog' in pr_labels:
        print('No changelog entries required (changelog/no-changelog label found)')
        return
    errors = get_changelog_errors(git_diff, changelog_entry_suffix(pr_number, pr_url))
    parser.add_argument('--pr-file')
    import argparse
