from .other import get_sex_choices

get_func_by_command = {
	1: "start",
	2: "post",
	3: "get",
	4: "post_advanced",
	5: "get_advanced",
	6: "update_db"
}

language_code = 'en'  # ru/en

sex_choices = get_sex_choices(language_code)

