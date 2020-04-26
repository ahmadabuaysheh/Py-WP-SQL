import shutil


def wpposts(post_id, post_content, post_title, post_excerpt, post_type, website_url):
    post_author = 1
    post_date = "2020-04-10 00:00:00"
    post_status = "publish"
    comment_status = "closed"
    ping_status = "closed"
    post_password = ""
    post_name = post_title.replace(" ", "-")
    to_ping = ""
    pinged = ""
    post_content_filtered = ""
    post_parent = 0
    guid = website_url + f"/p={post_id}"
    menu_order = 0
    post_mime_type = ""
    comment_count = 0

    sql_string = f"INSERT INTO `wp_posts`(`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, " \
                 f"`post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, " \
                 f"`post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, " \
                 f"`post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) " \
                 f"VALUES ('{post_id}','{post_author}','{post_date}','{post_date}','{post_content}'," \
                 f"'{post_title}','{post_excerpt}','{post_status}','{comment_status}','{ping_status}','{post_password}'," \
                 f"'{post_name}','{to_ping}','{pinged}','{post_date}','{post_date}','{post_content_filtered}'," \
                 f"'{post_parent}','{guid}','{menu_order}','{post_type}','{post_mime_type}','{comment_count}'); \r\n"

    return sql_string


def wpposts_meta(postid, meta_type, value):
    if meta_type == 'image':
        custom_field = "_thumbnail_id"
    else:
        custom_field = meta_type

    sql_string = f"INSERT INTO `wp_postmeta`(`post_id`, `meta_key`, `meta_value`) " \
                 f"VALUES ('{postid}','{custom_field}','{value}'); \r\n"
    return sql_string


def wpposts_meta_cf(postid, key, keyid, value):
    value = value.replace("'", "\\\'")
    sql_string = f"INSERT INTO `wp_postmeta`(`post_id`, `meta_key`, `meta_value`) " \
                 f"VALUES ('{postid}','{key}','{value}'); \r\n" \
                 f"INSERT INTO `wp_postmeta`(`post_id`, `meta_key`, `meta_value`) " \
                 f"VALUES ('{postid}','_{key}','{keyid}'); \r\n"
    return sql_string
