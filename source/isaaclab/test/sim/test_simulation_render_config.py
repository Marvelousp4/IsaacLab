# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause


"""Launch Isaac Sim Simulator first."""

from isaaclab.app import AppLauncher, run_tests

# launch omniverse app
app_launcher = AppLauncher(headless=True, enable_cameras=True)
simulation_app = app_launcher.app

"""Rest everything follows."""

import toml
import unittest

import carb
import flatdict
from isaacsim.core.utils.carb import get_carb_setting

from isaaclab.sim.simulation_cfg import RenderCfg, SimulationCfg
from isaaclab.sim.simulation_context import SimulationContext


class TestSimulationRenderConfig(unittest.TestCase):
    """Tests for simulation context render config."""

    """
    Tests
    """

    def test_render_cfg(self):
        """Test that the simulation context is created with the correct render cfg."""
        enable_translucency = True
        enable_reflections = True
        enable_global_illumination = True
        antialiasing_mode = "DLAA"
        enable_dlssg = True
        enable_dl_denoiser = True
        dlss_mode = 0
        enable_direct_lighting = True
        samples_per_pixel = 4
        enable_shadows = True
        enable_ambient_occlusion = True

        render_cfg = RenderCfg(
            enable_translucency=enable_translucency,
            enable_reflections=enable_reflections,
            enable_global_illumination=enable_global_illumination,
            antialiasing_mode=antialiasing_mode,
            enable_dlssg=enable_dlssg,
            dlss_mode=dlss_mode,
            enable_dl_denoiser=enable_dl_denoiser,
            enable_direct_lighting=enable_direct_lighting,
            samples_per_pixel=samples_per_pixel,
            enable_shadows=enable_shadows,
            enable_ambient_occlusion=enable_ambient_occlusion,
        )

        cfg = SimulationCfg(render=render_cfg)

        sim = SimulationContext(cfg)

        self.assertEqual(sim.cfg.render.enable_translucency, enable_translucency)
        self.assertEqual(sim.cfg.render.enable_reflections, enable_reflections)
        self.assertEqual(sim.cfg.render.enable_global_illumination, enable_global_illumination)
        self.assertEqual(sim.cfg.render.antialiasing_mode, antialiasing_mode)
        self.assertEqual(sim.cfg.render.enable_dlssg, enable_dlssg)
        self.assertEqual(sim.cfg.render.dlss_mode, dlss_mode)
        self.assertEqual(sim.cfg.render.enable_dl_denoiser, enable_dl_denoiser)
        self.assertEqual(sim.cfg.render.enable_direct_lighting, enable_direct_lighting)
        self.assertEqual(sim.cfg.render.samples_per_pixel, samples_per_pixel)
        self.assertEqual(sim.cfg.render.enable_shadows, enable_shadows)
        self.assertEqual(sim.cfg.render.enable_ambient_occlusion, enable_ambient_occlusion)

        carb_settings_iface = carb.settings.get_settings()
        self.assertEqual(carb_settings_iface.get("/rtx/translucency/enabled"), sim.cfg.render.enable_translucency)
        self.assertEqual(carb_settings_iface.get("/rtx/reflections/enabled"), sim.cfg.render.enable_reflections)
        self.assertEqual(
            carb_settings_iface.get("/rtx/indirectDiffuse/enabled"), sim.cfg.render.enable_global_illumination
        )
        self.assertEqual(carb_settings_iface.get("/rtx-transient/dlssg/enabled"), sim.cfg.render.enable_dlssg)
        self.assertEqual(
            carb_settings_iface.get("/rtx-transient/dldenoiser/enabled"), sim.cfg.render.enable_dl_denoiser
        )
        self.assertEqual(carb_settings_iface.get("/rtx/post/dlss/execMode"), sim.cfg.render.dlss_mode)
        self.assertEqual(carb_settings_iface.get("/rtx/directLighting/enabled"), sim.cfg.render.enable_direct_lighting)
        self.assertEqual(
            carb_settings_iface.get("/rtx/directLighting/sampledLighting/samplesPerPixel"),
            sim.cfg.render.samples_per_pixel,
        )
        self.assertEqual(carb_settings_iface.get("/rtx/shadows/enabled"), sim.cfg.render.enable_shadows)
        self.assertEqual(
            carb_settings_iface.get("/rtx/ambientOcclusion/enabled"), sim.cfg.render.enable_ambient_occlusion
        )
        self.assertEqual(carb_settings_iface.get("/rtx/post/aa/op"), 4)  # dlss = 3, dlaa=4

    def test_render_cfg_defaults(self):
        """Test that the simulation context is created with the correct render cfg."""
        enable_translucency = False
        enable_reflections = False
        enable_global_illumination = False
        antialiasing_mode = "DLSS"
        enable_dlssg = False
        enable_dl_denoiser = False
        dlss_mode = 2
        enable_direct_lighting = False
        samples_per_pixel = 1
        enable_shadows = False
        enable_ambient_occlusion = False

        render_cfg = RenderCfg(
            enable_translucency=enable_translucency,
            enable_reflections=enable_reflections,
            enable_global_illumination=enable_global_illumination,
            antialiasing_mode=antialiasing_mode,
            enable_dlssg=enable_dlssg,
            enable_dl_denoiser=enable_dl_denoiser,
            dlss_mode=dlss_mode,
            enable_direct_lighting=enable_direct_lighting,
            samples_per_pixel=samples_per_pixel,
            enable_shadows=enable_shadows,
            enable_ambient_occlusion=enable_ambient_occlusion,
        )

        cfg = SimulationCfg(render=render_cfg)

        sim = SimulationContext(cfg)

        self.assertEqual(sim.cfg.render.enable_translucency, enable_translucency)
        self.assertEqual(sim.cfg.render.enable_reflections, enable_reflections)
        self.assertEqual(sim.cfg.render.enable_global_illumination, enable_global_illumination)
        self.assertEqual(sim.cfg.render.antialiasing_mode, antialiasing_mode)
        self.assertEqual(sim.cfg.render.enable_dlssg, enable_dlssg)
        self.assertEqual(sim.cfg.render.enable_dl_denoiser, enable_dl_denoiser)
        self.assertEqual(sim.cfg.render.dlss_mode, dlss_mode)
        self.assertEqual(sim.cfg.render.enable_direct_lighting, enable_direct_lighting)
        self.assertEqual(sim.cfg.render.samples_per_pixel, samples_per_pixel)
        self.assertEqual(sim.cfg.render.enable_shadows, enable_shadows)
        self.assertEqual(sim.cfg.render.enable_ambient_occlusion, enable_ambient_occlusion)

        carb_settings_iface = carb.settings.get_settings()
        self.assertEqual(carb_settings_iface.get("/rtx/translucency/enabled"), sim.cfg.render.enable_translucency)
        self.assertEqual(carb_settings_iface.get("/rtx/reflections/enabled"), sim.cfg.render.enable_reflections)
        self.assertEqual(
            carb_settings_iface.get("/rtx/indirectDiffuse/enabled"), sim.cfg.render.enable_global_illumination
        )
        self.assertEqual(carb_settings_iface.get("/rtx-transient/dlssg/enabled"), sim.cfg.render.enable_dlssg)
        self.assertEqual(
            carb_settings_iface.get("/rtx-transient/dldenoiser/enabled"), sim.cfg.render.enable_dl_denoiser
        )
        self.assertEqual(carb_settings_iface.get("/rtx/post/dlss/execMode"), sim.cfg.render.dlss_mode)
        self.assertEqual(carb_settings_iface.get("/rtx/directLighting/enabled"), sim.cfg.render.enable_direct_lighting)
        self.assertEqual(
            carb_settings_iface.get("/rtx/directLighting/sampledLighting/samplesPerPixel"),
            sim.cfg.render.samples_per_pixel,
        )
        self.assertEqual(carb_settings_iface.get("/rtx/shadows/enabled"), sim.cfg.render.enable_shadows)
        self.assertEqual(
            carb_settings_iface.get("/rtx/ambientOcclusion/enabled"), sim.cfg.render.enable_ambient_occlusion
        )
        self.assertEqual(carb_settings_iface.get("/rtx/post/aa/op"), 3)  # dlss = 3, dlaa=4

    def test_render_cfg_presets(self):
        """Test that the simulation context is created with the correct render cfg preset with overrides."""

        # carb setting dictionary overrides
        carb_settings = {"/rtx/raytracing/subpixel/mode": 3, "/rtx/pathtracing/maxSamplesPerLaunch": 999999}
        # user-friendly setting overrides
        dlss_mode = ("/rtx/post/dlss/execMode", 5)

        rendering_modes = ["performance", "balanced", "quality", "xr"]

        for rendering_mode in rendering_modes:
            # grab groundtruth preset settings
            preset_filename = f"apps/rendering_modes/{rendering_mode}.kit"
            with open(preset_filename) as file:
                preset_dict = toml.load(file)
            preset_dict = dict(flatdict.FlatDict(preset_dict, delimiter="."))

            render_cfg = RenderCfg(
                rendering_mode=rendering_mode,
                dlss_mode=dlss_mode[1],
                carb_settings=carb_settings,
            )

            cfg = SimulationCfg(render=render_cfg)

            SimulationContext(cfg)

            carb_settings_iface = carb.settings.get_settings()
            for key, val in preset_dict.items():
                setting_name = "/" + key.replace(".", "/")  # convert to carb setting format

                if setting_name in carb_settings:
                    # grab groundtruth from carb setting dictionary overrides
                    setting_gt = carb_settings[setting_name]
                elif setting_name == dlss_mode[0]:
                    # grab groundtruth from user-friendly setting overrides
                    setting_gt = dlss_mode[1]
                else:
                    # grab groundtruth from preset
                    setting_gt = val

                setting_val = get_carb_setting(carb_settings_iface, setting_name)

                self.assertEqual(setting_gt, setting_val)


if __name__ == "__main__":
    run_tests()
