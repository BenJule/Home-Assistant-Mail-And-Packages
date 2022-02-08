"""Constants for tests."""

FAKE_CONFIG_DATA_BAD = {
    "folder": '"INBOX"',
    "generate_mp4": "false",
    "gif_duration": 5,
    "host": None,
    "image_name": "mail_today.gif",
    "image_path": "/config/www/mail_and_packages/",
    "image_security": False,
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "amazon_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "mail_updated",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "zpackages_delivered",
        "zpackages_transit",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "amazon_delivered",
        "auspost_delivered",
        "auspost_packages",
        "auspost_delivering",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}

FAKE_CONFIG_DATA = {
    "amazon_days": 3,
    "amazon_fwds": "fakeuser@fake.email, fakeuser2@fake.email",
    "custom_img": False,
    "folder": '"INBOX"',
    "generate_mp4": False,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "image_path": "/config/www/mail_and_packages/",
    "image_security": True,
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "zpackages_delivered",
        "zpackages_transit",
        "amazon_delivered",
        "amazon_exception",
        "amazon_hub",
        "amazon_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "hermes_delivered",
        "hermes_delivering",
        "mail_updated",
        "royal_delivered",
        "royal_delivering",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}

FAKE_CONFIG_DATA_EXTERNAL = {
    "allow_external": True,
    "amazon_days": 3,
    "amazon_fwds": "fakeuser@fake.email, fakeuser2@fake.email",
    "custom_img": False,
    "folder": '"INBOX"',
    "generate_mp4": False,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "image_path": "custom_components/mail_and_packages/images/",
    "image_security": True,
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "zpackages_delivered",
        "zpackages_transit",
        "amazon_delivered",
        "amazon_hub",
        "amazon_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "hermes_delivered",
        "hermes_delivering",
        "mail_updated",
        "royal_delivered",
        "royal_delivering",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}

FAKE_CONFIG_DATA_CORRECTED_EXTERNAL = {
    "allow_external": True,
    "amazon_days": 3,
    "amazon_fwds": ["fakeuser@fake.email", "fakeuser2@fake.email"],
    "custom_img": False,
    "folder": '"INBOX"',
    "generate_mp4": False,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "image_path": "custom_components/mail_and_packages/images/",
    "image_security": True,
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "amazon_delivered",
        "amazon_hub",
        "amazon_packages",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
        "hermes_delivered",
        "hermes_delivering",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "mail_updated",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "royal_delivered",
        "royal_delivering",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "zpackages_delivered",
        "zpackages_transit",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}

FAKE_CONFIG_DATA_CORRECTED = {
    "allow_external": False,
    "amazon_days": 3,
    "amazon_fwds": ["fakeuser@fake.email", "fakeuser2@fake.email"],
    "custom_img": False,
    "folder": '"INBOX"',
    "generate_mp4": False,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "image_path": "custom_components/mail_and_packages/images/",
    "image_security": True,
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "amazon_delivered",
        "amazon_exception",
        "amazon_hub",
        "amazon_packages",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
        "hermes_delivered",
        "hermes_delivering",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "mail_updated",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "royal_delivered",
        "royal_delivering",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "zpackages_delivered",
        "zpackages_transit",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}

FAKE_CONFIG_DATA_NO_PATH = {
    "amazon_fwds": ["fakeuser@fake.email", "fakeuser2@fake.email"],
    "custom_img": False,
    "folder": '"INBOX"',
    "generate_mp4": False,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "amazon_delivered",
        "amazon_exception",
        "amazon_hub",
        "amazon_packages",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
        "hermes_delivered",
        "hermes_delivering",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "mail_updated",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "royal_delivered",
        "royal_delivering",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "zpackages_delivered",
        "zpackages_transit",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}

FAKE_CONFIG_DATA_NO_RND = {
    "amazon_days": 3,
    "amazon_fwds": ["fakeuser@fake.email"],
    "custom_img": False,
    "folder": '"INBOX"',
    "generate_mp4": True,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "image_path": "custom_components/mail_and_packages/images/",
    "image_security": False,
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "amazon_delivered",
        "amazon_hub",
        "amazon_packages",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "mail_updated",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
        "zpackages_delivered",
        "zpackages_transit",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}

FAKE_CONFIG_DATA_MP4 = {
    "amazon_fwds": ["fakeuser@fake.email"],
    "custom_img": False,
    "folder": '"INBOX"',
    "generate_mp4": True,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "image_path": "/config/custom_components/mail_and_packages/images/",
    "image_security": True,
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "amazon_delivered",
        "amazon_packages",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "mail_updated",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "zpackages_delivered",
        "zpackages_transit",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}

FAKE_UPDATE_DATA = {
    "image_name": "mail_today.gif",
    "mail_updated": "2022-01-06T12:14:38+00:00",
    "usps_mail": 6,
    "usps_delivered": 3,
    "usps_delivering": 3,
    "usps_packages": 3,
    "usps_tracking": ["92123456789012345"],
    "ups_delivered": 1,
    "ups_delivering": 1,
    "ups_packages": 1,
    "ups_tracking": ["1Z123456789"],
    "fedex_delivered": 0,
    "fedex_delivering": 2,
    "fedex_packages": 2,
    "fedex_tracking": ["1234567890"],
    "amazon_packages": 7,
    "amazon_delivered": 2,
    "amazon_order": ["#123-4567890"],
    "amazon_hub": 2,
    "amazon_hub_code": 123456,
    "capost_delivered": 1,
    "capost_delivering": 1,
    "capost_packages": 2,
    "dhl_delivered": 0,
    "dhl_delivering": 1,
    "dhl_packages": 2,
    "dhl_tracking": ["1234567890"],
    "zpackages_delivered": 7,
    "zpackages_transit": 8,
    "auspost_delivered": 2,
    "auspost_delivering": 1,
    "auspost_packages": 3,
    "poczta_polska_delivering": 1,
    "poczta_polska_packages": 1,
    "inpost_pl_delivered": 2,
    "inpost_pl_delivering": 1,
    "inpost_pl_packages": 3,
    "inpost_pl_tracking": ["520113017830399002575123"],
    "dpd_com_pl_delivered": 2,
    "dpd_com_pl_delivering": 1,
    "dpd_com_pl_packages": 3,
    "dpd_com_pl_tracking": ["13490015284111"],
    "gls_delivered": 2,
    "gls_delivering": 1,
    "gls_packages": 3,
    "gls_tracking": ["51687952111"],
}

FAKE_CONFIG_DATA_MISSING_TIMEOUT = {
    "amazon_fwds": "fakeuser@fake.email, fakeuser2@fake.email",
    "custom_img": False,
    "folder": '"INBOX"',
    "generate_mp4": False,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "image_path": "/config/custom_components/mail_and_packages/images/",
    "image_security": True,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "zpackages_delivered",
        "zpackages_transit",
        "amazon_delivered",
        "amazon_hub",
        "amazon_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "hermes_delivered",
        "hermes_delivering",
        "mail_updated",
        "royal_delivered",
        "royal_delivering",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}

FAKE_CONFIG_DATA_AMAZON_FWD_STRING = {
    "allow_external": True,
    "amazon_fwds": "fakeuser@fake.email",
    "custom_img": False,
    "folder": '"INBOX"',
    "generate_mp4": False,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "image_path": "custom_components/mail_and_packages/images/",
    "image_security": True,
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "zpackages_delivered",
        "zpackages_transit",
        "amazon_delivered",
        "amazon_hub",
        "amazon_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "hermes_delivered",
        "hermes_delivering",
        "mail_updated",
        "royal_delivered",
        "royal_delivering",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}
FAKE_CONFIG_DATA_CUSTOM_IMG = {
    "allow_external": False,
    "amazon_fwds": ["fakeuser@fake.email", "fakeuser2@fake.email"],
    "custom_img": True,
    "custom_img_file": "images/test.gif",
    "folder": '"INBOX"',
    "generate_mp4": False,
    "gif_duration": 5,
    "host": "imap.test.email",
    "image_name": "mail_today.gif",
    "image_path": "custom_components/mail_and_packages/images/",
    "image_security": True,
    "imap_timeout": 30,
    "password": "suchfakemuchpassword",
    "port": 993,
    "resources": [
        "amazon_delivered",
        "amazon_exception",
        "amazon_hub",
        "amazon_packages",
        "capost_delivered",
        "capost_delivering",
        "capost_packages",
        "dhl_delivered",
        "dhl_delivering",
        "dhl_packages",
        "fedex_delivered",
        "fedex_delivering",
        "fedex_packages",
        "hermes_delivered",
        "hermes_delivering",
        "mail_updated",
        "royal_delivered",
        "royal_delivering",
        "ups_delivered",
        "ups_delivering",
        "ups_packages",
        "usps_delivered",
        "usps_delivering",
        "usps_mail",
        "usps_packages",
        "zpackages_delivered",
        "zpackages_transit",
        "auspost_delivered",
        "auspost_delivering",
        "auspost_packages",
        "poczta_polska_delivering",
        "poczta_polska_packages",
        "inpost_pl_delivered",
        "inpost_pl_delivering",
        "inpost_pl_packages",
        "dpd_com_pl_delivered",
        "dpd_com_pl_delivering",
        "dpd_com_pl_packages",
        "gls_delivered",
        "gls_delivering",
        "gls_packages",
    ],
    "scan_interval": 20,
    "username": "user@fake.email",
}
