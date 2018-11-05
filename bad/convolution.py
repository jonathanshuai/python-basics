import numpy as np

class ConvLayer():
    def __init__(self, width=3, height=3, channels=3, n_filters=8, stride=1, padding=0):
        self.width = width
        self.height = height
        self.channels = channels
        self.n_filters = n_filters
        self.stride = stride
        self.padding = 0

        self.filters = np.random.randn(height, width, channels, n_filters)



    def apply(self, input_volume):
        # input_volume.shape = (H, W, C)

        H = input_volume.shape[0]
        W = input_volume.shape[1]

        assert input_volume.shape[2] == self.channels

        padded_input = np.pad(input_volume, self.padding, 'constant')

        H_o = (H + 2 * self.padding - self.height) // 2 + 1
        W_o = (W + 2 * self.padding - self.width) // 2 + 1

        output_volume = np.zeros((H_o, W_o, self.n_filters))


        for i in range(self.n_filters):
            for j in range(0, output_volume.shape[0], self.stride):
                for k in range(0, output_volume.shape[1], self.stride):
                    min_h_j = j
                    max_h_j = min_h_j + self.height

                    min_w_k = k
                    max_w_k = min_w_k + self.width

                    output_volume[j, k, i] = np.sum(input_volume[min_h_j:max_h_j, min_w_k:max_w_k, :] * self.filters[:, :, :, i])

        return output_volume


cl = ConvLayer()
ov = cl.apply(np.random.randn(5, 5, 3))