package genetic.data.serializers;

public class BestIndividualToExcelFormatConverter {

    private final int variableNumber;
    public BestIndividualToExcelFormatConverter(int variableNumber) {
        this.variableNumber = variableNumber;
    }

    public String convert(String bestIndividual, int rowNumber) {

        //  O(N^2) but it's not a problem since N is small
        for (int i = 0; i < this.variableNumber; ++i) {
            bestIndividual = bestIndividual.replace("X" + Integer.toString(i + 1),  Character.toString('A' + i) + rowNumber);
        }

        return bestIndividual;
    }
}
