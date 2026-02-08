from electinfo_common import UrlPatterns


def test_candidate_president():
    assert UrlPatterns.candidate.president("joe-biden") == "/candidates/president/us/joe-biden/"


def test_candidate_senate():
    assert UrlPatterns.candidate.senate("CA", "john-smith") == "/candidates/senate/ca/john-smith/"


def test_candidate_senate_lowercase_passthrough():
    assert UrlPatterns.candidate.senate("ca", "john-smith") == "/candidates/senate/ca/john-smith/"


def test_candidate_house():
    assert UrlPatterns.candidate.house("CA", "12", "jane-doe") == "/candidates/house/ca-12/jane-doe/"


def test_candidate_house_zero_padded():
    assert UrlPatterns.candidate.house("NY", "1", "john-doe") == "/candidates/house/ny-01/john-doe/"


def test_committee():
    assert UrlPatterns.committee("super-pac", "my-pac", "C00123456") == "/committees/super-pac/my-pac-c00123456/"


def test_individual():
    assert UrlPatterns.individual("john-smith", "I-abcdef123456") == "/individuals/john-smith-i-abcdef123456/"


def test_individual_without_prefix():
    assert UrlPatterns.individual("john-smith", "abcdef123456extra") == "/individuals/john-smith-i-abcdef123456/"


def test_employer():
    assert UrlPatterns.employer("acme-corp", "O-abc123") == "/employers/acme-corp-abc123/"


def test_vendor():
    assert UrlPatterns.vendor("media-co", "V-def456") == "/vendors/media-co-def456/"


def test_party():
    assert UrlPatterns.party("democratic-party") == "/parties/democratic-party/"


def test_district():
    assert UrlPatterns.district("ca-12") == "/districts/ca-12/"


def test_state():
    assert UrlPatterns.state("california") == "/states/california/"


def test_cycle():
    assert UrlPatterns.cycle(2024) == "/elections/2024/"
    assert UrlPatterns.cycle("2024") == "/elections/2024/"
