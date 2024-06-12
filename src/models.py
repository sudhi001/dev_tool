from objectbox.model import Entity, Id,String


@Entity()
class ConsoleOutput:
    id = Id()
    build_number = String()
    project_name = String()
    build_date = String()
    generated_by = String()
    console_output = String()
    revision_msg = String()
    result = String()
    duration = String()
    flavour = String()
    revision = String()
    apk_url = String()

