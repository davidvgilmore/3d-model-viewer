# 3D Model Viewer

This project demonstrates a simple 3D model viewer using the <model-viewer> component from [modelviewer.dev](https://modelviewer.dev/).

## Features

- Renders a 3D model of an astronaut
- Allows camera controls for user interaction
- Auto-rotates the model for a dynamic display

## Usage

1. Open the `index.html` file in a web browser.
2. Interact with the 3D model using your mouse or touch controls:
   - Click and drag to rotate the model
   - Scroll to zoom in and out
   - Right-click and drag to pan the view

## Customization

To use your own 3D model:

1. Replace the `src` attribute in the <model-viewer> tag with the URL or path to your .glb or .gltf file.
2. Adjust the `alt` attribute to describe your model.

Example:

```html
<model-viewer src="path/to/your/model.glb"
              alt="A 3D model of your object"
              auto-rotate
              camera-controls>
</model-viewer>
```

## Dependencies

This project uses the <model-viewer> web component, which is loaded from unpkg.com in the HTML file.

