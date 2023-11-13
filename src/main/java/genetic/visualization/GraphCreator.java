package genetic.visualization;


import java.awt.*;
import java.io.IOException;

public interface GraphCreator {
    void create();
    void save() throws IOException, AWTException, InterruptedException;
}