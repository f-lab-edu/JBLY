import multiprocessing
import importlib

sub_directory_name = "urlCollection"


def run_job(module_name):
    module_name = sub_directory_name + "." + module_name
    module = importlib.import_module(module_name)
    return module.gather_urls()


def url_collecting():
    module_names = ['morecherry_urls_collector', 'theverlin_urls_collector', 'porterna_urls_collector']
    output = []
    with multiprocessing.Pool(3) as pool:
        results = pool.imap(run_job, module_names)
        for result in results:
            output.append(result)
    return output
