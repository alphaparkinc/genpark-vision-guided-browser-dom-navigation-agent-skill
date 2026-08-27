from client import VisionGuidedBrowserDomNavigationAgentClient

def main():
    client = VisionGuidedBrowserDomNavigationAgentClient()
    res = client.execute_browser_automation_flow('https://supplier-portal.com/reports', 'Export annual inventory audits')
    print('Browser Automation: ' + res['automation_run_id'] + ' | ' + res['target_url'])
    print('DOM Elements Interacted: ' + str(res['dom_elements_interacted_count']) + ' (CAPTCHA Solved: ' + str(res['captcha_solved_rate_pct']) + '%)')
    print('Vision Grounded Clicks: ' + str(res['vision_grounded_clicks_verified']) + ' | Artifacts: ' + str(res['artifacts_downloaded_count']))
    print('Session Video: ' + res['screen_recording_mp4_url'])

if __name__ == '__main__':
    main()
