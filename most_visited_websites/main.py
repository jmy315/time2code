"""
idea:
1) read each line and store each website as key  into a dict
2) if website is in dict, +1 to value
3) if webiste is not in dict, set value to 0
4) turn dict into list of (website, count) tuples
5) sort list by count
6) return first 5 websites

Complexity: O(N^2) where N is num of words inside the file
"""
from absl import app

def main(argv):
    print(top_websites(argv[1]))
    return

def top_websites(file):
    dic = {}
    with open(file, 'r') as fd:
        for line in fd:
            sites = line.split()[1:]
            for site in sites:
                if site not in dic:
                    dic[site] = 0
                dic[site] += 1
    tuples = [(k, v) for k, v in dic.items()]
    ranks = sorted(tuples, key=lambda c: c[1], reverse=True)
    return [s for s,_ in ranks[:5]]

if __name__ == '__main__':
    app.run(main)
