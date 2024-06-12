import os

from src.JenkinsManager import JenkinsManager


# Main function


def load_CI(jenkins_manager):
    projects = jenkins_manager.list_jenkins_projects()
    if projects:
        print("Jenkins Projects:")
        for project in projects:
            print(f"- {project}")

    # Step 3: Get Last Build Report for NectoMobilePackage
    project_name = "NectoMobilePackage"
    last_build_report = jenkins_manager.get_last_build_report(project_name)

    if last_build_report:
        print(f"Last Build Report for {project_name}:")
        print(last_build_report)
        last_build_number = last_build_report['number']
        folder = f'../data/{project_name}/{last_build_number}/'
        jenkins_manager.write_json_to_file(last_build_report, folder, 'last_build_report.json')

        # Step 4: Get Build Console Output
        console_output = jenkins_manager.get_build_console_output(project_name, last_build_number)
        print(f"Build Console Output for Build Number {last_build_number}:")
        print(console_output)
        apk_url = jenkins_manager.extract_apk_url(console_output)
        # Save console output to file
        with open(os.path.join(folder, 'build_console_output.txt'), 'w') as f:
            f.write(console_output)
        # Store console output in ObjectBox
        jenkins_manager.store_console_output(last_build_number, project_name, console_output, last_build_report,
                                             apk_url)
        if apk_url:
            print(f"APK URL found: {apk_url}")
            jenkins_manager.download_file(folder, apk_url)
        else:
            print("No APK URL found in the console output.")
    else:
        print(f"Failed to retrieve the last build report for {project_name}.")


# Main function
if __name__ == "__main__":
    jenkins_manager = JenkinsManager('../config.toml')
    load_CI(jenkins_manager)
    jenkins_manager.loadALL()
