import matplotlib.pyplot as plt
from skimage import measure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patches as mpatches
import ipywidgets as widgets


def plot_3d(
    image,
    label="label",
    color="cornflowerblue",
    alpha=0.5,
    level=None,
    title="",
):
    """
    3D plot.

    Arguments:
    image : ndarray
        List of masks to overlay.
    label : str
        Name of plot.
    color : str
        Color of plot.
    alpha : float
        Opacity of plot.
    threshold : num

    title : str
        Main title of a whole plot.
    """

    fig = plt.figure(figsize=(12, 5))
    fig.suptitle(title, fontsize=16)
    ax = fig.add_subplot(111, projection="3d")
    patches = []

    image = image.transpose(2, 0, 1)
    image = image[:, :, ::-1]

    ax.set_xlim(0, image.shape[0])
    ax.set_ylim(0, image.shape[1])
    ax.set_zlim(0, image.shape[2])

    verts, faces, _, _ = measure.marching_cubes(image, level=level)

    mesh = Poly3DCollection(verts[faces], alpha=alpha)
    face_color = color
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)
    patches.append(mpatches.Patch(color=color, label=label))
    ax.legend(handles=patches)
    plt.show()


def slices_slider(image, initial_slice, title=""):
    @widgets.interact(axial_slice=(0, image.shape[0] - 1))
    def axial_slicer(axial_slice=initial_slice):
        _, ax = plt.subplots(1, 1, figsize=(7, 7))
        ax.imshow(image[axial_slice, :, :], cmap="bone")
        ax.set_title(title)
        ax.axis("off")
        plt.show()


def main():
    pass


if __name__ == "__main__":
    main()
