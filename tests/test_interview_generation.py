import os

from docassemble.l4.intgen import generate_interview

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files',
)


def test_generate_interview_rsp():
    with open('test_files/rps.pl') as scasp:
        with open('test_files/rps.yml') as yml:
            output = generate_interview(yml.read(), scasp.read())
            print(output)


def test_generate_interview_r34():
    with open('test_files/r34.pl', encoding='utf-8') as scasp:
        with open('test_files/r34.yml', encoding='utf-8') as yml:
            with open('test_files/r34.da.yml', encoding='utf-8') as interview_yml:
                output = generate_interview(yml.read(), scasp.read())
                assert interview_yml.read() == output
