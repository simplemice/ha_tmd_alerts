import aiohttp
import xml.etree.ElementTree as ET
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession


async def fetch_warnings(hass: HomeAssistant, url: str, uid: str, ukey: str) -> list[dict]:
    session = async_get_clientsession(hass)
    timeout = aiohttp.ClientTimeout(total=30)

    async with session.get(url, params={"uid": uid, "ukey": ukey}, timeout=timeout) as resp:
        resp.raise_for_status()
        text = await resp.text(encoding="utf-8")

    root = ET.fromstring(text)
    warnings = []

    for warning in root.findall(".//Warning"):
        warnings.append({
            "issue_no": warning.findtext("IssueNo", ""),
            "effect_start": warning.findtext("EffectStartDate", ""),
            "effect_end": warning.findtext("EffectEndDate", ""),
            "announce_date": warning.findtext("AnnounceDate", ""),
            "title_en": warning.findtext("TitleEnglish", ""),
            "headline_en": warning.findtext("HeadlineEnglish", ""),
            "description_en": warning.findtext("DescriptionEnglish", ""),
            "title_th": warning.findtext("TitleThai", ""),
            "headline_th": warning.findtext("HeadlineThai", ""),
            "url_en": warning.findtext("WebUrlEnglish", ""),
            "url_th": warning.findtext("WebUrlThai", ""),
            "contact": warning.findtext("ContactEnglish", ""),
        })

    return warnings
