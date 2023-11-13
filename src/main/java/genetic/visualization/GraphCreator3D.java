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
import org.jzy3d.colors.Color;
import org.jzy3d.colors.ColorMapper;
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

public class GraphCreator3D  extends AWTAbstractAnalysis implements GraphCreator {

    private File savePath;
    private final InputData inputData;
    private final ExcelData excelInputData;
    private Chart graph;
    public GraphCreator3D(File savePath, InputData inputData, ExcelData excelInputData) {
        this.savePath = savePath;
        this.inputData = inputData;
        this.excelInputData = excelInputData;
    }

    @Override
    public void create() {
        Func3D func = new Func3D((x, y) -> x * Math.sin(x * y));
        Range range = new Range(-3, 3);
        int steps = 80;

        var dataTinyGP = new ArrayList<Coord3d>();
        var dataFunction = new ArrayList<Coord3d>();

        for (int i = 0; i < this.excelInputData.calculatedValues().size(); ++i) {
            var TinyGPPoint = new Coord3d(this.inputData.targets()[i][0], this.inputData.targets()[i][1], this.excelInputData.calculatedValues().get(i));
            dataTinyGP.add(TinyGPPoint);
            var functionPoint = new Coord3d(this.inputData.targets()[i][0], this.inputData.targets()[i][1], this.inputData.targets()[i][2]);
            dataFunction.add(functionPoint);
        }

        // Create the object to represent the function over the given range.
        final var surface = new SurfaceBuilder().delaunay(dataFunction);
        surface.setColorMapper(new ColorMapper(new ColorMapRBG(), surface, new Color(1, 1, 1, .5f)));
        surface.setFaceDisplayed(true);
        surface.setWireframeDisplayed(true);
        surface.setWireframeColor(Color.WHITE);

        // Create a chart
        IChartFactory f = new AWTChartFactory();
        this.chart = f.newChart(Quality.Advanced().setHiDPIEnabled(true));
        this.chart.getScene().getGraph().add(surface);
        this.chart.getView().setViewPositionMode(ViewPositionMode.PROFILE);
        this.chart.open();
        this.chart.addMouse();
    }

    @Override
    public void save() throws IOException, AWTException {
        Settings.getInstance().setHardwareAccelerated(true);
        chart.getCanvas().setPixelScale(new float[] { 1, 1 });
        chart.getCanvas().screenshot(this.savePath);
    }

    @Override
    public void init() throws Exception {

    }
}
