# cmmsApp/urls.py

from django.urls import path
from . import views


app_name = "cmmsApp"


urlpatterns = [

    # =========================================================
    # MAIN PAGES
    # =========================================================

    # Home
    path(
        "",
        views.home,
        name="home"
    ),

    # About
    path(
        "about/",
        views.about,
        name="about"
    ),

    # Contact page
    path(
        "contact/",
        views.contact,
        name="contact"
    ),


    # =========================================================
    # REQUEST DEMO
    # =========================================================

    path(
        "request-demo/",
        views.request_demo_view,
        name="request_demo"
    ),


    # =========================================================
    # CHANGE BY JYOTI - 10-Sep-2026
    # EMAIL OTP VERIFICATION - START
    # =========================================================

    # Called when user clicks "Verify email"
    path(
        "api/contact/send-email-otp/",
        views.send_email_otp,
        name="send_email_otp"
    ),

    # Called when user enters OTP and clicks "Verify OTP"
    path(
        "api/contact/verify-email-otp/",
        views.verify_email_otp,
        name="verify_email_otp"
    ),

    # =========================================================
    # CHANGE BY JYOTI - EMAIL OTP VERIFICATION - END
    # =========================================================


    # =========================================================
    # CONTACT FORM
    # =========================================================

    # Contact block form submission
    #
    # Used in contact_block.html:
    #
    # {% url 'cmmsApp:contact_submit' %}
    #
    path(
        "contact/submit/",
        views.contact_block_submit,
        name="contact_submit"
    ),


    # =========================================================
    # CONTACT HELPERS
    # =========================================================

    # Phone / country detection
    path(
        "contact/phone-info/",
        views.phone_info,
        name="phone_info"
    ),

    # Country dropdown list
    path(
        "contact/country-list/",
        views.country_list,
        name="country_list"
    ),


    # =========================================================
    # THANK YOU PAGE
    # =========================================================

    path(
        "thanks/",
        views.contact_thanks,
        name="contact_thanks"
    ),


    # =========================================================
    # SITEMAP
    # =========================================================

    path(
        "sitemap.xml",
        views.sitemap,
        name="sitemap"
    ),

]