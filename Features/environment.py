from selenium import webdriver


Debug = False


def setup_debug_on_error(userdata):
    global Debug
    Debug = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    setup_debug_on_error(context.config.userdata)
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()
    context.browser.get("https://github.com")


def after_all(context):
    context.browser.quit()


def after_step(context, step):
    if Debug and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_scenario(context, scenario):
    context.browser.get("https://github.com")
