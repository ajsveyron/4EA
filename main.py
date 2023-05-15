from sys import exit, argv
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QMainWindow, QGridLayout, QWidget, QLabel, \
    QLineEdit, QSizePolicy, QLayout, QScrollArea, QGroupBox, QListWidget, QListWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as numpty
import antropy as ent
from scipy import signal
from scipy.integrate import simps

class WaveBox(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.amplitude_label = QLabel('Amplitude')
        self.amplitude_label.setParent(self)
        self.amplitude_label.adjustSize()
        self.amplitude_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.layout.addWidget(self.amplitude_label)

        self.amplitude_entry = QLineEdit()
        self.amplitude_entry.setParent(self)
        self.layout.addWidget(self.amplitude_entry)

        self.frequency_label = QLabel('Frequency')
        self.frequency_label.setParent(self)
        self.frequency_label.adjustSize()
        self.frequency_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.layout.addWidget(self.frequency_label)

        self.frequency_entry = QLineEdit()
        self.frequency_entry.setParent(self)
        self.layout.addWidget(self.frequency_entry)

        self.phase_label = QLabel('Phase')
        self.phase_label.setParent(self)
        self.phase_label.adjustSize()
        self.phase_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.layout.addWidget(self.phase_label)

        self.phase_entry = QLineEdit()
        self.phase_entry.setParent(self)
        self.layout.addWidget(self.phase_entry)

        self.time_label = QLabel('Time')
        self.time_label.setParent(self)
        self.time_label.adjustSize()
        self.time_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.layout.addWidget(self.time_label)

        self.time_entry = QLineEdit()
        self.time_entry.setParent(self)
        self.layout.addWidget(self.time_entry)


class StatBox(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.labels = []

        self.delta_label = QLabel('Delta:')
        self.delta_label.setParent(self)

        self.delta_power = QLabel('')
        self.delta_power.setParent(self)
        self.labels.append(self.delta_power)

        self.theta_label = QLabel('Theta:')
        self.theta_label.setParent(self)

        self.theta_power = QLabel('')
        self.theta_power.setParent(self)
        self.labels.append(self.theta_power)

        self.alpha_label = QLabel('Alpha:')
        self.alpha_label.setParent(self)

        self.alpha_power = QLabel('')
        self.alpha_power.setParent(self)
        self.labels.append(self.alpha_power)

        self.beta_label = QLabel('Beta:')
        self.beta_label.setParent(self)

        self.beta_power = QLabel('')
        self.beta_power.setParent(self)
        self.labels.append(self.beta_power)

        self.gamma_label = QLabel('Gamma:')
        self.gamma_label.setParent(self)

        self.gamma_power = QLabel('')
        self.gamma_power.setParent(self)
        self.labels.append(self.gamma_power)

        self.delta_w_label = QLabel('Delta_w:')
        self.delta_w_label.setParent(self)

        self.delta_w_power = QLabel('')
        self.delta_w_power.setParent(self)
        self.labels.append(self.delta_w_power)

        self.theta_w_label = QLabel('Theta_w:')
        self.theta_w_label.setParent(self)

        self.theta_w_power = QLabel('')
        self.theta_w_power.setParent(self)
        self.labels.append(self.theta_w_power)

        self.alpha_w_label = QLabel('Alpha_w:')
        self.alpha_w_label.setParent(self)

        self.alpha_w_power = QLabel('')
        self.alpha_w_power.setParent(self)
        self.labels.append(self.alpha_w_power)

        self.beta_w_label = QLabel('Beta_w:')
        self.beta_w_label.setParent(self)

        self.beta_w_power = QLabel('')
        self.beta_w_power.setParent(self)
        self.labels.append(self.beta_w_power)

        self.gamma_w_label = QLabel('Gamma_w:')
        self.gamma_w_label.setParent(self)

        self.gamma_w_power = QLabel('')
        self.gamma_w_power.setParent(self)
        self.labels.append(self.gamma_w_power)

        self.entropy_label = QLabel('Entropy')
        self.entropy_label.setParent(self)

        self.entropy = QLabel('')
        self.entropy.setParent(self)
        self.labels.append(self.entropy)

        self.layout.addWidget(self.delta_label, 0, 0)
        self.layout.addWidget(self.delta_power, 0, 1)
        self.layout.addWidget(self.theta_label, 1, 0)
        self.layout.addWidget(self.theta_power, 1, 1)
        self.layout.addWidget(self.alpha_label, 2, 0)
        self.layout.addWidget(self.alpha_power, 2, 1)
        self.layout.addWidget(self.beta_label, 3, 0)
        self.layout.addWidget(self.beta_power, 3, 1)
        self.layout.addWidget(self.gamma_label, 4, 0)
        self.layout.addWidget(self.gamma_power, 4, 1)
        self.layout.addWidget(self.delta_w_label, 5, 0)
        self.layout.addWidget(self.delta_w_power, 5, 1)
        self.layout.addWidget(self.theta_w_label, 6, 0)
        self.layout.addWidget(self.theta_w_power, 6, 1)
        self.layout.addWidget(self.alpha_w_label, 7, 0)
        self.layout.addWidget(self.alpha_w_power, 7, 1)
        self.layout.addWidget(self.beta_w_label, 8, 0)
        self.layout.addWidget(self.beta_w_power, 8, 1)
        self.layout.addWidget(self.gamma_w_label, 9, 0)
        self.layout.addWidget(self.gamma_w_power, 9, 1)
        self.layout.addWidget(self.entropy_label, 10, 0)
        self.layout.addWidget(self.entropy, 10, 1)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.waves = []

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.wave_1 = WaveBox()
        self.wave_1.setParent(self)

        self.power = StatBox()
        self.power.setParent(self)

        self.plot_btn = QPushButton('plot')
        self.plot_btn.setParent(self)
        self.plot_btn.clicked.connect(self.plot)

        self.clear_btn = QPushButton('clear')
        self.clear_btn.setParent(self)
        self.clear_btn.clicked.connect(self.clear)

        self.figure_1 = plt.figure()
        self.canvas_1 = FigureCanvas(self.figure_1)

        self.figure_2 = plt.figure()
        self.canvas_2 = FigureCanvas(self.figure_2)

        self.figure_3 = plt.figure()
        self.canvas_3 = FigureCanvas(self.figure_3)

        self.layout.addWidget(self.wave_1, 0, 0)
        self.layout.addWidget(self.clear_btn, 2, 0)
        self.layout.addWidget(self.plot_btn, 1, 0)
        self.layout.addWidget(self.power, 3, 0)
        self.layout.addWidget(self.canvas_1, 0, 1, 15, 3)
        self.layout.addWidget(self.canvas_2, 15, 1, 15, 3)
        self.layout.addWidget(self.canvas_3, 0, 4, 30, 3)

    def plot(self):
        # print(self.amplitude_entry.text())
        self.plot_btn.setText('add wave')
        amplitude = float(self.wave_1.amplitude_entry.text())
        frequency = float(self.wave_1.frequency_entry.text())
        phase = float(self.wave_1.phase_entry.text())
        time = int(self.wave_1.time_entry.text())
        print(time)

        srate = 256

        x = numpty.arange(int(time*srate))
        print(x)
        y = amplitude*numpty.sin((2*numpty.pi*frequency*x/256) + phase)

        self.waves.append(y)

        self.figure_1.clear()
        self.figure_2.clear()
        self.figure_3.clear()

        combined_wave = numpty.zeros(y.shape)
        ax_1 = self.figure_1.add_subplot(111)

        for y in self.waves:
            ax_1.plot(x, y)

            combined_wave += y


        ax_2 = self.figure_2.add_subplot(111)
        ax_2.plot(x, combined_wave)

        frequencies = numpty.fft.fftfreq(len(combined_wave), 1/256)[0:int(len(combined_wave)/2)]
        fft = numpty.array(numpty.abs(numpty.fft.fft(combined_wave))[0:int(len(combined_wave)/2)])

        ax_3 = self.figure_3.add_subplot(111)
        ax_3.plot(frequencies, fft)

        print(numpty.max(numpty.abs(numpty.fft.fft(y))[0:int(len(y)/2)]))

        print('FREQUENCIES: ', numpty.fft.fftfreq(len(combined_wave), 1/256)[0:int(len(combined_wave)/2)])

        entropy = ent.spectral_entropy(combined_wave, 256, 'fft')
        self.power.entropy.setText(f'{entropy}')

        freqs_welch, psd = signal.welch(combined_wave, 256)
        freq_res = freqs_welch[3] - freqs_welch[2]

        delta_start = numpty.array(numpty.nonzero(frequencies >= 1.0))[0, 0]
        delta_stop = numpty.array(numpty.nonzero(frequencies >= 4.0))[0, 0]
        idx_delta = numpty.logical_and(freqs_welch >= 1.0, freqs_welch <= 4.0)

        theta_start = numpty.array(numpty.nonzero(frequencies >= 4.01))[0, 0]
        theta_stop = numpty.array(numpty.nonzero(frequencies >= 7.0))[0, 0]
        idx_theta = numpty.logical_and(freqs_welch >= 4.01, freqs_welch <= 7.0)

        alpha_start = numpty.array(numpty.nonzero(frequencies >= 7.01))[0, 0]
        alpha_stop = numpty.array(numpty.nonzero(frequencies >= 13.0))[0, 0]
        idx_alpha = numpty.logical_and(freqs_welch >= 7.01, freqs_welch <= 13.0)

        beta_start = numpty.array(numpty.nonzero(frequencies >= 13.01))[0, 0]
        beta_stop = numpty.array(numpty.nonzero(frequencies >= 30.0))[0, 0]
        idx_beta = numpty.logical_and(freqs_welch >= 13.01, freqs_welch <= 30.0)

        gamma_start = numpty.array(numpty.nonzero(frequencies >= 30.01))[0, 0]
        gamma_stop = numpty.array(numpty.nonzero(frequencies >= 48.0))[0, 0]
        idx_gamma = numpty.logical_and(freqs_welch >= 30.01, freqs_welch <= 48.0)

        # print(int(delta_start))

        delta = numpty.mean(fft[int(delta_start):int(delta_stop)])
        print('delta', delta)
        self.power.delta_power.setText(f'{delta:.2f}')

        delta_w = simps(psd[idx_delta], dx=freq_res)
        self.power.delta_w_power.setText(f'{delta_w:.2f}')
        print('delta_w', delta_w)

        theta = numpty.mean(fft[int(theta_start):int(theta_stop)])
        self.power.theta_power.setText(f'{theta:.2f}')

        theta_w = simps(psd[idx_theta], dx=freq_res)
        self.power.theta_w_power.setText(f'{theta_w:.2f}')

        alpha = numpty.mean(fft[int(alpha_start):int(alpha_stop)])
        self.power.alpha_power.setText(f'{alpha:.2f}')

        alpha_w = simps(psd[idx_alpha], dx=freq_res)
        self.power.alpha_w_power.setText(f'{alpha_w:.2f}')

        beta = numpty.mean(fft[int(beta_start):int(beta_stop)])
        self.power.beta_power.setText(f'{beta:.2f}')

        beta_w = simps(psd[idx_beta], dx=freq_res)
        self.power.beta_w_power.setText(f'{beta_w:.2f}')

        gamma = numpty.mean(fft[int(gamma_start):int(gamma_stop)])
        self.power.gamma_power.setText(f'{gamma:.2f}')

        gamma_w = simps(psd[idx_gamma], dx=freq_res)
        self.power.gamma_w_power.setText(f'{gamma_w:.2f}')

        self.canvas_1.draw()
        self.canvas_2.draw()
        self.canvas_3.draw()

        # print(numpty.fft.fftfreq(len(y), 1/256)[numpty.argmax(numpty.abs(numpty.fft.fft(y))[:int(len(y)/2)])])
        print(freqs_welch, psd)

    def clear(self):

        self.figure_1.clear()
        self.figure_2.clear()
        self.figure_3.clear()

        self.canvas_1.draw()
        self.canvas_2.draw()
        self.canvas_3.draw()

        self.waves = []

        self.plot_btn.setText('plot')

        for stat in self.power.labels:
            stat.setText('0')


if __name__ == '__main__':
    # Create pyqt application
    app = QApplication(argv)

    # Create overall window (taskWindow object)
    window = Window()

    # Show the taskWindow object
    window.show()

    # Launch the app
    exit(app.exec_())





