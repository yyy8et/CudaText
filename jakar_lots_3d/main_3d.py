"""Minimal Ursina viewer for four schematic Jakar parcels."""

from ursina import (
    EditorCamera,
    Entity,
    Text,
    Ursina,
    camera,
    color,
    mouse,
    scene,
    window,
)


PARCELS = (
    {
        "lot_id": "Lot 2063",
        "position": (-4, 0, 4),
        "color": color.azure,
        "gps": None,
    },
    {
        "lot_id": "Lot 774",
        "position": (4, 0, 4),
        "color": color.orange,
        "gps": None,
    },
    {
        "lot_id": "Lot 618",
        "position": (-4, 0, -4),
        "color": color.lime,
        "gps": None,
    },
    {
        "lot_id": "Lot 619",
        "position": (4, 0, -4),
        "color": color.violet,
        "gps": None,
    },
)


app = Ursina()
window.title = "Jakar Delta - Parcel Viewer"

for parcel in PARCELS:
    lot = Entity(
        model="cube",
        name=parcel["lot_id"],
        color=parcel["color"],
        scale=(3, 0.5, 3),
        position=parcel["position"],
        collider="box",
    )
    lot.lot_id = parcel["lot_id"]
    lot.gps = parcel["gps"]

    Text(
        parcel["lot_id"],
        parent=scene,
        position=(parcel["position"][0], 2, parcel["position"][2]),
        scale=2,
        billboard=True,
        color=color.white,
        background=True,
    )

Text(
    "示意布局 · 地块 GPS 坐标待核实",
    parent=camera.ui,
    position=(-0.86, 0.46),
    scale=0.8,
    color=color.white,
)

EditorCamera(position=(0, 14, -20), rotation=(30, 0, 0))


def input(key: str) -> None:
    if key != "left mouse down":
        return

    lot = mouse.hovered_entity
    if lot is None or not hasattr(lot, "lot_id"):
        return

    x, y, z = (round(float(value), 2) for value in lot.position)
    gps = lot.gps
    gps_text = (
        f"{gps[0]:.8f}, {gps[1]:.8f}"
        if gps is not None
        else "待核实（未提供该地块的地理坐标）"
    )
    print(f"{lot.lot_id} | 场景 XYZ: ({x}, {y}, {z}) | WGS84: {gps_text}")


if __name__ == "__main__":
    app.run()
