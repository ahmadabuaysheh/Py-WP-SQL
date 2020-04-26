import urllib.parse as prs



def wpterms(termid, name):
    name = name.replace("'", "\\\'")
    slug = name.replace(' ', '-')
    slug = prs.quote(slug)
    sql_string = f"INSERT INTO `wp_terms`(`term_id`, `name`, `slug`) " \
                 f"VALUES ('{termid}','{name}','{slug}'); \r\n"
    return sql_string


def wpterm_taxonomy(termid, taxonomy, description, parent):
    description = description.replace("'", "\\\'")
    sql_string = f"INSERT INTO `wp_term_taxonomy`(`term_id`, `taxonomy`, `description`, `parent`) " \
                 f"VALUES ('{termid}','{taxonomy}','{description}','{parent}'); \n"
    return sql_string


def wpterm_meta(termid, key, value):
    sql_string = f"INSERT INTO `wp_termmeta`(`term_id`, `meta_key`, `meta_value`) " \
                 f"VALUES ('{termid}','{key}','{value}'); \r\n"
    return sql_string


def wpterm_meta_cf(termid, key, keyid, value):
    value = value.replace("'", "\\\'")
    sql_string = f"INSERT INTO `wp_termmeta`(`term_id`, `meta_key`, `meta_value`) " \
                 f"VALUES ('{termid}','{key}','{value}'); \r\n" \
                 f"INSERT INTO `wp_termmeta`(`term_id`, `meta_key`, `meta_value`) " \
                 f"VALUES ('{termid}','_{key}','{keyid}'); \r\n"
    return sql_string


def wpterm_relationships(objectid, term_taxonomy_id):
    sql_string = f"INSERT INTO `wp_term_relationships`(`object_id`, `term_taxonomy_id`) " \
                 f"VALUES ('{objectid}','{term_taxonomy_id}'); \r\n"
    return sql_string
