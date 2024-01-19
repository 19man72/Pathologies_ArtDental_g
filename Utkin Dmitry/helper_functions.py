ISSUES = {
    "Центральное": "normal",
    "Компрессия": "compression",
    "Дистракция": "distraction",
    "Дистальное": "distal",
    "Мезиальное": "mesial",
    "Латеральное": "lateral",
    "Медиальное": "medial",
}

PROJECTIONS = {
    "Аксиальная": "axial",
    "Сагитальная": "sagittal",
    "Корональная": "coronal",
}

PROJECTION_METRICS = {
    "axial": ["anterior", "posterior", "medial", "lateral"],
    "sagittal": ["anterior", "superior", "posterior"],
    "coronal": ["medial", "lateral", "superior"],
}


def get_issue(path):
    issue_name = path.split("/")[-1].split(" ")[1].split(".")[0]
    issue_id = ISSUES[issue_name]

    return issue_name, issue_id


def get_projection(path):
    projection_name = path.split("/")[-2].split(" ")[-2]
    projection_id = PROJECTIONS[projection_name]

    return projection_name, projection_id


def get_side(filename):
    if "Л" in filename:
        return "Слева", "left"
    elif "П" in filename:
        return "Справа", "right"


def get_metrics(projection_id):
    return PROJECTION_METRICS[projection_id]


def main():
    pass


if __name__ == "__main__":
    main()
