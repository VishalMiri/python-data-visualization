import requests

from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process the results.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    
    submission_dict = {
        'title': response_dict['title'],
        'link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)

# Sort the submissions by comment count.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Print the titles and comment counts of the top submissions.
for submission_dict in submission_dicts:
    print(f"Title: {submission_dict['title']}")
    print(f"Comments: {submission_dict['comments']}")
    print(f"Link: {submission_dict['link']}\n")