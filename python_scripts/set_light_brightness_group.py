# Set the parent and child light
parent_light = data.get("parent_light")
child_light = data.get("child_light")

# Get the brightness of the parent light.
parent_brightness = (hass.states.get(parent_light)).attributes['brightness']

# Set the brightness of the child light to match the parent light.
hass.services.call("light", "turn_on", {"entity_id": child_light, "brightness": parent_brightness}, False)