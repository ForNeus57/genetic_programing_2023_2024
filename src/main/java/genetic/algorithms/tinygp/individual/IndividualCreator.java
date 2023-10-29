package genetic.algorithms.tinygp.individual;

import genetic.algorithms.tinygp.TinyGP;

import java.util.Random;


public class IndividualCreator {
    private final char[] temporaryIndividualBody;
    private final Random randomDevice;
    private final int maximumTreeDepth;
    private final int variableNumber;
    private final int randomConstraintsSize;

    //  Random device is passed, because there is a need to make this deterministic for a random seed.
    public IndividualCreator(int maximumSizeOfIndividual, Random randomDevice, int maximumTreeDepth, int variableNumber, int randomConstraintsSize) {
        this.temporaryIndividualBody = new char[maximumSizeOfIndividual];
        this.randomDevice = randomDevice;
        this.maximumTreeDepth = maximumTreeDepth;
        this.variableNumber = variableNumber;
        this.randomConstraintsSize = randomConstraintsSize;
    }

    public Individual createRandomIndividual() {
        int len;

        do {
            //  I think we try to run it until created individual is valid, because randomness in grow function can mess up given individual.
            len = grow(this.temporaryIndividualBody, 0, this.temporaryIndividualBody.length, this.maximumTreeDepth);
        } while (len < 0);                                           //  -1 from grow function means algorithm fucked up

        var ind = new char[len];

        System.arraycopy(this.temporaryIndividualBody, 0, ind, 0, len);

        return new Individual(ind);
    }

    private int grow(char [] buffer, int pos, int max, int depth) {
        char prim = (char) this.randomDevice.nextInt(2);   //  Why 2???? - Returns either 0 or 1

        if (pos >= max)
            return -1;

        if (pos == 0)
            prim = 1;

        if ( prim == 0 || depth == 0 ) {
            //  No clue what is being randomized here
            prim = (char) this.randomDevice.nextInt(this.variableNumber + this.randomConstraintsSize);
            buffer[pos] = prim;
            return pos + 1;
        }   //  There was an else here. I have removed it because unnecessary nesting.

        prim = (char) (this.randomDevice.nextInt(TinyGP.FSET_END - TinyGP.FSET_START + 1) + TinyGP.FSET_START);     //  Choose random operation

        //  Removed funny switch here...
        buffer[pos] = prim;
        var one_child = grow(buffer, pos + 1, max, depth - 1);              //  If one child is invalid then all the rest
        if (one_child < 0)
            return -1;

        return grow(buffer, one_child, max, depth - 1);
    }
}
