package genetic.visualization;

import com.jogamp.opengl.util.stereo.ViewerPose;
import com.jogamp.opengl.util.texture.Texture;
import com.jogamp.opengl.util.texture.TextureData;
import com.jogamp.opengl.util.texture.TextureIO;
import genetic.data.ExcelData;
import genetic.data.InputData;
import org.jzy3d.analysis.AWTAbstractAnalysis;
import org.jzy3d.chart.Chart;
import org.jzy3d.chart.ChartLauncher;
import org.jzy3d.chart.Settings;
import org.jzy3d.chart.factories.AWTChartFactory;
import org.jzy3d.chart.factories.IChartFactory;
import org.jzy3d.chart.factories.IFrame;
import org.jzy3d.colors.Color;
import org.jzy3d.colors.ColorMapper;
import org.jzy3d.colors.colormaps.ColorMapGrayscale;
import org.jzy3d.colors.colormaps.ColorMapRBG;
import org.jzy3d.colors.colormaps.ColorMapRainbow;
import org.jzy3d.maths.Coord3d;
import org.jzy3d.maths.Range;
import org.jzy3d.plot3d.builder.Func3D;
import org.jzy3d.plot3d.builder.SurfaceBuilder;
import org.jzy3d.plot3d.builder.concrete.OrthonormalGrid;
import org.jzy3d.plot3d.rendering.canvas.Quality;
import org.jzy3d.plot3d.rendering.view.modes.ViewPositionMode;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.image.RenderedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class GraphCreator3D  extends AWTAbstractAnalysis {

    private File savePath;
    private final InputData inputData;
    private final ExcelData excelInputData;
    private Chart graph;
    public GraphCreator3D(File savePath, InputData inputData, ExcelData excelInputData) {
        this.savePath = savePath;
        this.inputData = inputData;
        this.excelInputData = excelInputData;
    }

    public void create() throws IOException, InterruptedException, AWTException {
        var dataTinyGP = new ArrayList<Coord3d>();
        var dataFunction = new ArrayList<Coord3d>();

        for (int i = 0; i < this.excelInputData.calculatedValues().size(); ++i) {
            var TinyGPPoint = new Coord3d(this.inputData.targets()[i][0], this.inputData.targets()[i][1], this.excelInputData.calculatedValues().get(i));
            dataTinyGP.add(TinyGPPoint);
            var functionPoint = new Coord3d(this.inputData.targets()[i][0], this.inputData.targets()[i][1], this.inputData.targets()[i][2]);
            dataFunction.add(functionPoint);
        }

        var data = new ArrayList<ArrayList<Coord3d>>();
        data.add(dataTinyGP);
        data.add(dataFunction);

        var modes = new ArrayList<ViewPositionMode>();
        modes.add(ViewPositionMode.PROFILE);
        modes.add(ViewPositionMode.FREE);
        modes.add(ViewPositionMode.YZ);
        modes.add(ViewPositionMode.XZ);
        modes.add(ViewPositionMode.TOP);

        var extension = new ArrayList<String>();
        extension.add("tiny_gp");
        extension.add("function");

        for (int i = 0; i < data.size(); ++i) {
            for (var mode : modes) {
                var chart = this.createChart(data.get(i), mode);
                chart.open("Graph");
                this.save(chart, new File(savePath.getAbsolutePath() + "_" + extension.get(i)+ "_" + mode.toString() + ".png"));
                chart.dispose();
            }
        }
    }

    private Chart createChart(ArrayList<Coord3d> data, ViewPositionMode mode) {
        // Create the object to represent the function over the given range.
        final var surface = new SurfaceBuilder().delaunay(data);
        surface.setColorMapper(new ColorMapper(new ColorMapRBG(), surface, new Color(1, 1, 1, .5f)));
        surface.setFaceDisplayed(true);
        surface.setWireframeDisplayed(true);
        surface.setWireframeColor(Color.BLACK);

        // Create a chart
        IChartFactory f = new AWTChartFactory();
        var chart = f.newChart(Quality.Advanced().setHiDPIEnabled(true));
        chart.getScene().getGraph().add(surface);
        chart.getView().setViewPositionMode(mode);
        chart.getView().setMaximized(true);

        return chart;
    }

    public void save(Chart chart, File savePath) throws IOException, AWTException, InterruptedException {
        Thread.sleep(200);
        double x = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice().getDisplayMode().getWidth();
        double y = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice().getDisplayMode().getHeight();

        Image image = new Robot()
            .createMultiResolutionScreenCapture(new Rectangle(
                5,
                0,
                chart.getCanvas().getRendererWidth(),
                chart.getCanvas().getRendererHeight() + 30)
            )
            .getResolutionVariant(x, y);
        ImageIO.write((BufferedImage) image, "png", savePath);
    }

    @Override
    public void init() throws Exception {

    }
}
