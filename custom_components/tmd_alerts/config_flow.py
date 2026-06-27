import aiohttp
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import API_URL, CONF_UID, CONF_UKEY, DEFAULT_UID, DEFAULT_UKEY, DOMAIN


class TMDConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            uid = user_input.get(CONF_UID) or DEFAULT_UID
            ukey = user_input.get(CONF_UKEY) or DEFAULT_UKEY

            try:
                session = async_get_clientsession(self.hass)
                timeout = aiohttp.ClientTimeout(total=10)
                async with session.get(
                    API_URL,
                    params={"uid": uid, "ukey": ukey},
                    timeout=timeout,
                ) as resp:
                    if resp.status != 200:
                        errors["base"] = "cannot_connect"
                    else:
                        return self.async_create_entry(
                            title="Thailand Weather Alerts (TMD)",
                            data={CONF_UID: uid, CONF_UKEY: ukey},
                        )
            except aiohttp.ClientError:
                errors["base"] = "cannot_connect"
            except Exception:  # noqa: BLE001
                errors["base"] = "unknown"

        schema = vol.Schema({
            vol.Optional(CONF_UID, default=DEFAULT_UID): str,
            vol.Optional(CONF_UKEY, default=DEFAULT_UKEY): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
