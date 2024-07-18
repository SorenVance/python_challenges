<Profile xmlns="http://schemas.datacontract.org/2004/07/NINA.Profile"
         xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
    <AlpacaSettings i:type="AlpacaSettings">
        <DiscoveryDuration>2</DiscoveryDuration>
        <DiscoveryPort>32227</DiscoveryPort>
        <NumberOfPolls>1</NumberOfPolls>
        <PollInterval>100</PollInterval>
        <ResolveDnsName>false</ResolveDnsName>
        <UseHttps>false</UseHttps>
        <UseIPv4>true</UseIPv4>
        <UseIPv6>false</UseIPv6>
    </AlpacaSettings>
    <ApplicationSettings i:type="ApplicationSettings">
        <Culture>en-GB</Culture>
        <DevicePollingInterval>2</DevicePollingInterval>
        <LogLevel>INFO</LogLevel>
        <PageSize>50</PageSize>
        <SelectedPluggableBehaviors xmlns:a="http://schemas.datacontract.org/2004/07/System.Collections.Generic">
            <a:KeyValuePairOfstringstring>
                <a:key>NINA.WPF.Base.Interfaces.IAutoFocusVMFactory</a:key>
                <a:value>NINA.Joko.Plugins.HocusFocus.AutoFocus.HocusFocusVMFactory</a:value>
            </a:KeyValuePairOfstringstring>
            <a:KeyValuePairOfstringstring>
                <a:key>NINA.Image.ImageAnalysis.IStarAnnotator</a:key>
                <a:value>NINA.Joko.Plugins.HocusFocus.StarDetection.HocusFocusStarAnnotator</a:value>
            </a:KeyValuePairOfstringstring>
            <a:KeyValuePairOfstringstring>
                <a:key>NINA.Image.ImageAnalysis.IStarDetection</a:key>
                <a:value>NINA.Joko.Plugins.HocusFocus.StarDetection.HocusFocusStarDetection</a:value>
            </a:KeyValuePairOfstringstring>
        </SelectedPluggableBehaviors>
        <SkyAtlasImageRepository>C:\NINA\SkyAtlasImageRepository</SkyAtlasImageRepository>
        <SkySurveyCacheDirectory>C:\NINA\FramingAssistantCache</SkySurveyCacheDirectory>
    </ApplicationSettings>
    <AstrometrySettings i:type="AstrometrySettings">
        <Elevation>1456</Elevation>
        <HorizonFilePath/>
        <Latitude>39.0777297</Latitude>
        <Longitude>-108.6651261</Longitude>
    </AstrometrySettings>
    <CameraSettings i:type="CameraSettings">
        <ASCOMAllowUnevenPixelDimension>true</ASCOMAllowUnevenPixelDimension>
        <ASCOMCreate32BitData>false</ASCOMCreate32BitData>
        <AtikExposureSpeed>0</AtikExposureSpeed>
        <AtikGainPreset>0</AtikGainPreset>
        <AtikWindowHeaterPowerLevel>0</AtikWindowHeaterPowerLevel>
        <BadPixelCorrection>true</BadPixelCorrection>
        <BadPixelCorrectionThreshold>60</BadPixelCorrectionThreshold>
        <BayerPattern>Auto</BayerPattern>
        <BinAverageEnabled>false</BinAverageEnabled>
        <BinningX i:nil="true"/>
        <BinningY i:nil="true"/>
        <BitDepth>16</BitDepth>
        <BitScaling>true</BitScaling>
        <BulbMode>NATIVE</BulbMode>
        <CoolingDuration>0</CoolingDuration>
        <DewHeaterOn>true</DewHeaterOn>
        <FLIEnableFloodFlush>false</FLIEnableFloodFlush>
        <FLIEnableSnapshotFloodFlush>false</FLIEnableSnapshotFloodFlush>
        <FLIFloodBin i:nil="true" xmlns:a="http://schemas.datacontract.org/2004/07/NINA.Core.Model.Equipment"/>
        <FLIFloodDuration>1</FLIFloodDuration>
        <FLIFlushCount>2</FLIFlushCount>
        <FileCameraAlwaysListen>false</FileCameraAlwaysListen>
        <FileCameraDownloadDelay>0</FileCameraDownloadDelay>
        <FileCameraExtension>ALL</FileCameraExtension>
        <FileCameraFolder/>
        <FileCameraIsBayered>false</FileCameraIsBayered>
        <FileCameraUseBulbMode>false</FileCameraUseBulbMode>
        <Gain>119</Gain>
        <GenericCameraDewHeaterStrength>10</GenericCameraDewHeaterStrength>
        <GenericCameraFanSpeed>70</GenericCameraFanSpeed>
        <Id>ZWO ASI2600MC Duo #1</Id>
        <MaxFlatExposureTime>1</MaxFlatExposureTime>
        <MinFlatExposureTime>0.2</MinFlatExposureTime>
        <MirrorLockupDelay>0</MirrorLockupDelay>
        <Offset>50</Offset>
        <PixelSize>3.76</PixelSize>
        <QhyIncludeOverscan>false</QhyIncludeOverscan>
        <RawConverter>FREEIMAGE</RawConverter>
        <ReadoutMode i:nil="true"/>
        <ReadoutModeForNormalImages i:nil="true"/>
        <ReadoutModeForSnapImages i:nil="true"/>
        <SBIGUseExternalCcdTracker>false</SBIGUseExternalCcdTracker>
        <SerialPort>COM1</SerialPort>
        <Temperature>-10</Temperature>
        <Timeout>60</Timeout>
        <TouptekAlikeDewHeaterStrength>-1</TouptekAlikeDewHeaterStrength>
        <TouptekAlikeHighFullwell>false</TouptekAlikeHighFullwell>
        <TouptekAlikeLEDLights>true</TouptekAlikeLEDLights>
        <TouptekAlikeUltraMode>true</TouptekAlikeUltraMode>
        <TrackingCameraASCOMServerEnabled>false</TrackingCameraASCOMServerEnabled>
        <TrackingCameraASCOMServerLoggingEnabled>false</TrackingCameraASCOMServerLoggingEnabled>
        <TrackingCameraASCOMServerPipeName>NINA.ASCOM.Camera.SBIG.Tracker</TrackingCameraASCOMServerPipeName>
        <USBLimit>90</USBLimit>
        <WarmingDuration>0</WarmingDuration>
        <ZwoAsiMonoBinMode>false</ZwoAsiMonoBinMode>
    </CameraSettings>
    <ColorSchemaSettings i:type="ColorSchemaSettings">
        <AltColorSchema xmlns:a="http://schemas.datacontract.org/2004/07/NINA.Core.Utility.ColorSchema">
            <a:BackgroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>0</b:B>
                <b:G>0</b:G>
                <b:R>0</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0</b:ScB>
                <b:ScG>0</b:ScG>
                <b:ScR>0</b:ScR>
            </a:BackgroundColor>
            <a:BorderColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>24</b:B>
                <b:G>12</b:G>
                <b:R>85</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.009134059</b:ScB>
                <b:ScG>0.0036765074</b:ScG>
                <b:ScR>0.09084172</b:ScR>
            </a:BorderColor>
            <a:ButtonBackgroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>52</b:B>
                <b:G>93</b:G>
                <b:R>255</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.034339808</b:ScB>
                <b:ScG>0.10946172</b:ScG>
                <b:ScR>1</b:ScR>
            </a:ButtonBackgroundColor>
            <a:ButtonBackgroundSelectedColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>26</b:B>
                <b:G>3</b:G>
                <b:R>150</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.010329823</b:ScB>
                <b:ScG>0.000910581</b:ScG>
                <b:ScR>0.30498734</b:ScR>
            </a:ButtonBackgroundSelectedColor>
            <a:ButtonForegroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>0</b:B>
                <b:G>0</b:G>
                <b:R>0</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0</b:ScB>
                <b:ScG>0</b:ScG>
                <b:ScR>0</b:ScR>
            </a:ButtonForegroundColor>
            <a:ButtonForegroundDisabledColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>48</b:B>
                <b:G>55</b:G>
                <b:R>68</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.029556835</b:ScB>
                <b:ScG>0.038204372</b:ScG>
                <b:ScR>0.057805438</b:ScR>
            </a:ButtonForegroundDisabledColor>
            <a:Name>Alternative Custom</a:Name>
            <a:NotificationErrorColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>0</b:B>
                <b:G>0</b:G>
                <b:R>112</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0</b:ScB>
                <b:ScG>0</b:ScG>
                <b:ScR>0.16202939</b:ScR>
            </a:NotificationErrorColor>
            <a:NotificationErrorTextColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>10</b:B>
                <b:G>1</b:G>
                <b:R>2</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.00303527</b:ScB>
                <b:ScG>0.000303527</b:ScG>
                <b:ScR>0.000607054</b:ScR>
            </a:NotificationErrorTextColor>
            <a:NotificationWarningColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>11</b:B>
                <b:G>51</b:G>
                <b:R>94</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.0033465358</b:ScB>
                <b:ScG>0.033104766</b:ScG>
                <b:ScR>0.111932434</b:ScR>
            </a:NotificationWarningColor>
            <a:NotificationWarningTextColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>10</b:B>
                <b:G>1</b:G>
                <b:R>2</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.00303527</b:ScB>
                <b:ScG>0.000303527</b:ScG>
                <b:ScR>0.000607054</b:ScR>
            </a:NotificationWarningTextColor>
            <a:PrimaryColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>0</b:B>
                <b:G>0</b:G>
                <b:R>255</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0</b:ScB>
                <b:ScG>0</b:ScG>
                <b:ScR>1</b:ScR>
            </a:PrimaryColor>
            <a:SecondaryBackgroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>201</b:A>
                <b:B>9</b:B>
                <b:G>4</b:G>
                <b:R>35</b:R>
                <b:ScA>0.7882353</b:ScA>
                <b:ScB>0.002731743</b:ScB>
                <b:ScG>0.001214108</b:ScG>
                <b:ScR>0.016807377</b:ScR>
            </a:SecondaryBackgroundColor>
            <a:SecondaryColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>8</b:B>
                <b:G>8</b:G>
                <b:R>23</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.002428216</b:ScB>
                <b:ScG>0.002428216</b:ScG>
                <b:ScR>0.008568126</b:ScR>
            </a:SecondaryColor>
            <a:TertiaryBackgroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>13</b:B>
                <b:G>6</b:G>
                <b:R>45</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.004024717</b:ScB>
                <b:ScG>0.001821162</b:ScG>
                <b:ScR>0.026241222</b:ScR>
            </a:TertiaryBackgroundColor>
        </AltColorSchema>
        <ColorSchema xmlns:a="http://schemas.datacontract.org/2004/07/NINA.Core.Utility.ColorSchema">
            <a:BackgroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>0</b:B>
                <b:G>0</b:G>
                <b:R>0</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0</b:ScB>
                <b:ScG>0</b:ScG>
                <b:ScR>0</b:ScR>
            </a:BackgroundColor>
            <a:BorderColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>0</b:B>
                <b:G>153</b:G>
                <b:R>255</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0</b:ScB>
                <b:ScG>0.3185468</b:ScG>
                <b:ScR>1</b:ScR>
            </a:BorderColor>
            <a:ButtonBackgroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>0</b:B>
                <b:G>0</b:G>
                <b:R>255</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0</b:ScB>
                <b:ScG>0</b:ScG>
                <b:ScR>1</b:ScR>
            </a:ButtonBackgroundColor>
            <a:ButtonBackgroundSelectedColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>177</b:B>
                <b:G>183</b:G>
                <b:R>0</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.4396572</b:ScB>
                <b:ScG>0.4735315</b:ScG>
                <b:ScR>0</b:ScR>
            </a:ButtonBackgroundSelectedColor>
            <a:ButtonForegroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>255</b:B>
                <b:G>255</b:G>
                <b:R>255</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>1</b:ScB>
                <b:ScG>1</b:ScG>
                <b:ScR>1</b:ScR>
            </a:ButtonForegroundColor>
            <a:ButtonForegroundDisabledColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>127</b:B>
                <b:G>127</b:G>
                <b:R>127</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.21223076</b:ScB>
                <b:ScG>0.21223076</b:ScG>
                <b:ScR>0.21223076</b:ScR>
            </a:ButtonForegroundDisabledColor>
            <a:Name>High Contrast</a:Name>
            <a:NotificationErrorColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>0</b:B>
                <b:G>0</b:G>
                <b:R>112</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0</b:ScB>
                <b:ScG>0</b:ScG>
                <b:ScR>0.16202939</b:ScR>
            </a:NotificationErrorColor>
            <a:NotificationErrorTextColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>255</b:B>
                <b:G>255</b:G>
                <b:R>255</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>1</b:ScB>
                <b:ScG>1</b:ScG>
                <b:ScR>1</b:ScR>
            </a:NotificationErrorTextColor>
            <a:NotificationWarningColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>11</b:B>
                <b:G>51</b:G>
                <b:R>94</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.0033465358</b:ScB>
                <b:ScG>0.033104766</b:ScG>
                <b:ScR>0.111932434</b:ScR>
            </a:NotificationWarningColor>
            <a:NotificationWarningTextColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>255</b:B>
                <b:G>255</b:G>
                <b:R>255</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>1</b:ScB>
                <b:ScG>1</b:ScG>
                <b:ScR>1</b:ScR>
            </a:NotificationWarningTextColor>
            <a:PrimaryColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>255</b:B>
                <b:G>255</b:G>
                <b:R>255</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>1</b:ScB>
                <b:ScG>1</b:ScG>
                <b:ScR>1</b:ScR>
            </a:PrimaryColor>
            <a:SecondaryBackgroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>13</b:B>
                <b:G>9</b:G>
                <b:R>47</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.004024717</b:ScB>
                <b:ScG>0.002731743</b:ScG>
                <b:ScR>0.02842604</b:ScR>
            </a:SecondaryBackgroundColor>
            <a:SecondaryColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>177</b:B>
                <b:G>183</b:G>
                <b:R>0</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.4396572</b:ScB>
                <b:ScG>0.4735315</b:ScG>
                <b:ScR>0</b:ScR>
            </a:SecondaryColor>
            <a:TertiaryBackgroundColor xmlns:b="http://schemas.datacontract.org/2004/07/System.Windows.Media">
                <b:A>255</b:A>
                <b:B>25</b:B>
                <b:G>25</b:G>
                <b:R>25</b:R>
                <b:ScA>1</b:ScA>
                <b:ScB>0.009721218</b:ScB>
                <b:ScG>0.009721218</b:ScG>
                <b:ScR>0.009721218</b:ScR>
            </a:TertiaryBackgroundColor>
        </ColorSchema>
    </ColorSchemaSettings>
    <Description/>
    <DockPanelSettings i:type="DockPanelSettings">
        <CameraInfoOnly>false</CameraInfoOnly>
        <FilterWheelInfoOnly>false</FilterWheelInfoOnly>
        <FlatDeviceInfoOnly>false</FlatDeviceInfoOnly>
        <FocuserInfoOnly>false</FocuserInfoOnly>
        <RotatorInfoOnly>false</RotatorInfoOnly>
        <ShowImagingHistogram>true</ShowImagingHistogram>
        <SwitchInfoOnly>false</SwitchInfoOnly>
    </DockPanelSettings>
    <DomeSettings i:type="DomeSettings">
        <AzimuthTolerance_degrees>2</AzimuthTolerance_degrees>
        <CloseOnUnsafe>false</CloseOnUnsafe>
        <DecOffsetHorizontal_mm>0</DecOffsetHorizontal_mm>
        <DomeRadius_mm>0</DomeRadius_mm>
        <DomeSyncTimeoutSeconds>120</DomeSyncTimeoutSeconds>
        <FindHomeBeforePark>false</FindHomeBeforePark>
        <GemAxis_mm>0</GemAxis_mm>
        <Id>No_Device</Id>
        <LateralAxis_mm>0</LateralAxis_mm>
        <MountType>EQUATORIAL</MountType>
        <ParkDomeBeforeShutterMove>false</ParkDomeBeforeShutterMove>
        <ParkMountBeforeShutterMove>false</ParkMountBeforeShutterMove>
        <RefuseUnsafeShutterMove>false</RefuseUnsafeShutterMove>
        <RefuseUnsafeShutterOpenSansSafetyDevice>false</RefuseUnsafeShutterOpenSansSafetyDevice>
        <RotateDegrees>10</RotateDegrees>
        <ScopePositionEastWest_mm>0</ScopePositionEastWest_mm>
        <ScopePositionNorthSouth_mm>0</ScopePositionNorthSouth_mm>
        <ScopePositionUpDown_mm>0</ScopePositionUpDown_mm>
        <SettleTimeSeconds>1</SettleTimeSeconds>
        <SyncSlewDomeWhenMountSlews>false</SyncSlewDomeWhenMountSlews>
        <SynchronizeDuringMountSlew>false</SynchronizeDuringMountSlew>
    </DomeSettings>
    <FilterWheelSettings i:type="FilterWheelSettings">
        <DisableGuidingOnFilterChange>true</DisableGuidingOnFilterChange>
        <FilterWheelFilters xmlns:a="http://schemas.datacontract.org/2004/07/NINA.Core.Model.Equipment">
            <a:FilterInfo>
                <a:FlatWizardFilterSettings>
                    <a:Binning>
                        <a:_x>1</a:_x>
                        <a:_y>1</a:_y>
                    </a:Binning>
                    <a:FlatWizardMode>DYNAMICEXPOSURE</a:FlatWizardMode>
                    <a:Gain>-1</a:Gain>
                    <a:HistogramMeanTarget>0.5</a:HistogramMeanTarget>
                    <a:HistogramTolerance>0.1</a:HistogramTolerance>
                    <a:MaxAbsoluteFlatDeviceBrightness>100</a:MaxAbsoluteFlatDeviceBrightness>
                    <a:MaxFlatExposureTime>1</a:MaxFlatExposureTime>
                    <a:MinAbsoluteFlatDeviceBrightness>0</a:MinAbsoluteFlatDeviceBrightness>
                    <a:MinFlatExposureTime>0.2</a:MinFlatExposureTime>
                    <a:Offset>-1</a:Offset>
                </a:FlatWizardFilterSettings>
                <a:_autoFocusBinning>
                    <a:_x>1</a:_x>
                    <a:_y>1</a:_y>
                </a:_autoFocusBinning>
                <a:_autoFocusExposureTime>-1</a:_autoFocusExposureTime>
                <a:_autoFocusFilter>false</a:_autoFocusFilter>
                <a:_autoFocusGain>-1</a:_autoFocusGain>
                <a:_autoFocusOffset>-1</a:_autoFocusOffset>
                <a:_focusOffset>0</a:_focusOffset>
                <a:_name>UV/IR Cut</a:_name>
                <a:_position>0</a:_position>
            </a:FilterInfo>
            <a:FilterInfo>
                <a:FlatWizardFilterSettings>
                    <a:Binning>
                        <a:_x>1</a:_x>
                        <a:_y>1</a:_y>
                    </a:Binning>
                    <a:FlatWizardMode>DYNAMICEXPOSURE</a:FlatWizardMode>
                    <a:Gain>-1</a:Gain>
                    <a:HistogramMeanTarget>0.5</a:HistogramMeanTarget>
                    <a:HistogramTolerance>0.1</a:HistogramTolerance>
                    <a:MaxAbsoluteFlatDeviceBrightness>100</a:MaxAbsoluteFlatDeviceBrightness>
                    <a:MaxFlatExposureTime>30</a:MaxFlatExposureTime>
                    <a:MinAbsoluteFlatDeviceBrightness>0</a:MinAbsoluteFlatDeviceBrightness>
                    <a:MinFlatExposureTime>0.01</a:MinFlatExposureTime>
                    <a:Offset>-1</a:Offset>
                </a:FlatWizardFilterSettings>
                <a:_autoFocusBinning>
                    <a:_x>1</a:_x>
                    <a:_y>1</a:_y>
                </a:_autoFocusBinning>
                <a:_autoFocusExposureTime>-1</a:_autoFocusExposureTime>
                <a:_autoFocusFilter>false</a:_autoFocusFilter>
                <a:_autoFocusGain>-1</a:_autoFocusGain>
                <a:_autoFocusOffset>-1</a:_autoFocusOffset>
                <a:_focusOffset>9</a:_focusOffset>
                <a:_name>L-eXtreme</a:_name>
                <a:_position>1</a:_position>
            </a:FilterInfo>
            <a:FilterInfo>
                <a:FlatWizardFilterSettings>
                    <a:Binning>
                        <a:_x>1</a:_x>
                        <a:_y>1</a:_y>
                    </a:Binning>
                    <a:FlatWizardMode>DYNAMICEXPOSURE</a:FlatWizardMode>
                    <a:Gain>-1</a:Gain>
                    <a:HistogramMeanTarget>0.5</a:HistogramMeanTarget>
                    <a:HistogramTolerance>0.1</a:HistogramTolerance>
                    <a:MaxAbsoluteFlatDeviceBrightness>100</a:MaxAbsoluteFlatDeviceBrightness>
                    <a:MaxFlatExposureTime>2</a:MaxFlatExposureTime>
                    <a:MinAbsoluteFlatDeviceBrightness>0</a:MinAbsoluteFlatDeviceBrightness>
                    <a:MinFlatExposureTime>0.2</a:MinFlatExposureTime>
                    <a:Offset>-1</a:Offset>
                </a:FlatWizardFilterSettings>
                <a:_autoFocusBinning>
                    <a:_x>1</a:_x>
                    <a:_y>1</a:_y>
                </a:_autoFocusBinning>
                <a:_autoFocusExposureTime>-1</a:_autoFocusExposureTime>
                <a:_autoFocusFilter>false</a:_autoFocusFilter>
                <a:_autoFocusGain>-1</a:_autoFocusGain>
                <a:_autoFocusOffset>-1</a:_autoFocusOffset>
                <a:_focusOffset>-10</a:_focusOffset>
                <a:_name>L-Quad</a:_name>
                <a:_position>2</a:_position>
            </a:FilterInfo>
        </FilterWheelFilters>
        <Id>Manual Filter Wheel</Id>
        <Unidirectional>false</Unidirectional>
    </FilterWheelSettings>
    <FlatDeviceSettings i:type="FlatDeviceSettings">
        <FilterSettings xmlns:a="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/>
        <Id>ASCOM.Giotto.SecondaryCoverCalibrator</Id>
        <Name i:nil="true"/>
        <PortName>AUTO</PortName>
        <SettleTime>0</SettleTime>
        <TrainedFlatExposureSettings>
            <TrainedFlatExposureSetting>
                <Binning xmlns:a="http://schemas.datacontract.org/2004/07/NINA.Core.Model.Equipment">
                    <a:_x>1</a:_x>
                    <a:_y>1</a:_y>
                </Binning>
                <Brightness>12</Brightness>
                <Filter>2</Filter>
                <Gain>-1</Gain>
                <Offset>-1</Offset>
                <Time>2</Time>
            </TrainedFlatExposureSetting>
            <TrainedFlatExposureSetting>
                <Binning xmlns:a="http://schemas.datacontract.org/2004/07/NINA.Core.Model.Equipment">
                    <a:_x>1</a:_x>
                    <a:_y>1</a:_y>
                </Binning>
                <Brightness>62</Brightness>
                <Filter>0</Filter>
                <Gain>-1</Gain>
                <Offset>-1</Offset>
                <Time>1</Time>
            </TrainedFlatExposureSetting>
            <TrainedFlatExposureSetting>
                <Binning xmlns:a="http://schemas.datacontract.org/2004/07/NINA.Core.Model.Equipment">
                    <a:_x>1</a:_x>
                    <a:_y>1</a:_y>
                </Binning>
                <Brightness>60</Brightness>
                <Filter>-1</Filter>
                <Gain>-1</Gain>
                <Offset>-1</Offset>
                <Time>1</Time>
            </TrainedFlatExposureSetting>
        </TrainedFlatExposureSettings>
    </FlatDeviceSettings>
    <FlatWizardSettings i:type="FlatWizardSettings">
        <AltitudeSite>EAST</AltitudeSite>
        <DarkFlatCount>30</DarkFlatCount>
        <FlatCount>30</FlatCount>
        <FlatWizardMode>DYNAMICBRIGHTNESS</FlatWizardMode>
        <HistogramMeanTarget>0.5</HistogramMeanTarget>
        <HistogramTolerance>0.1</HistogramTolerance>
        <OpenForDarkFlats>true</OpenForDarkFlats>
    </FlatWizardSettings>
    <FocuserSettings i:type="FocuserSettings">
        <AutoFocusBinning>1</AutoFocusBinning>
        <AutoFocusCurveFitting>HYPERBOLIC</AutoFocusCurveFitting>
        <AutoFocusDisableGuiding>false</AutoFocusDisableGuiding>
        <AutoFocusExposureTime>4</AutoFocusExposureTime>
        <AutoFocusInitialOffsetSteps>4</AutoFocusInitialOffsetSteps>
        <AutoFocusInnerCropRatio>1</AutoFocusInnerCropRatio>
        <AutoFocusMethod>STARHFR</AutoFocusMethod>
        <AutoFocusNumberOfFramesPerPoint>1</AutoFocusNumberOfFramesPerPoint>
        <AutoFocusOuterCropRatio>1</AutoFocusOuterCropRatio>
        <AutoFocusStepSize>175</AutoFocusStepSize>
        <AutoFocusTimeoutSeconds>600</AutoFocusTimeoutSeconds>
        <AutoFocusTotalNumberOfAttempts>1</AutoFocusTotalNumberOfAttempts>
        <AutoFocusUseBrightestStars>0</AutoFocusUseBrightestStars>
        <BacklashCompensationModel>OVERSHOOT</BacklashCompensationModel>
        <BacklashIn>0</BacklashIn>
        <BacklashOut>50</BacklashOut>
        <ContrastDetectionMethod>Statistics</ContrastDetectionMethod>
        <FocuserSettleTime>1</FocuserSettleTime>
        <Id>ASCOM.DarkSkyGeek.VirtualFocuser</Id>
        <RSquaredThreshold>0.8</RSquaredThreshold>
        <UseFilterWheelOffsets>true</UseFilterWheelOffsets>
    </FocuserSettings>
    <FramingAssistantSettings i:type="FramingAssistantSettings">
        <CameraHeight>4176</CameraHeight>
        <CameraWidth>6248</CameraWidth>
        <FieldOfView>6.524333333333333</FieldOfView>
        <LastRotationAngle>150</LastRotationAngle>
        <LastSelectedImageSource>HIPS2FITS</LastSelectedImageSource>
        <Opacity>0</Opacity>
        <SaveImageInOfflineCache>true</SaveImageInOfflineCache>
    </FramingAssistantSettings>
    <GnssSettings i:type="GnssSettings">
        <GnssSource>PrimaLuceLabEagle</GnssSource>
    </GnssSettings>
    <GuiderSettings i:type="GuiderSettings">
        <AutoRetryStartGuiding>false</AutoRetryStartGuiding>
        <AutoRetryStartGuidingTimeoutSeconds>300</AutoRetryStartGuidingTimeoutSeconds>
        <DitherPixels>7</DitherPixels>
        <DitherRAOnly>false</DitherRAOnly>
        <GuideChartDeclinationColor xmlns:a="http://schemas.datacontract.org/2004/07/System.Windows.Media">
            <a:A>255</a:A>
            <a:B>0</a:B>
            <a:G>0</a:G>
            <a:R>255</a:R>
            <a:ScA>1</a:ScA>
            <a:ScB>0</a:ScB>
            <a:ScG>0</a:ScG>
            <a:ScR>1</a:ScR>
        </GuideChartDeclinationColor>
        <GuideChartRightAscensionColor xmlns:a="http://schemas.datacontract.org/2004/07/System.Windows.Media">
            <a:A>255</a:A>
            <a:B>255</a:B>
            <a:G>0</a:G>
            <a:R>0</a:R>
            <a:ScA>1</a:ScA>
            <a:ScB>1</a:ScB>
            <a:ScG>0</a:ScG>
            <a:ScR>0</a:ScR>
        </GuideChartRightAscensionColor>
        <GuideChartShowCorrections>true</GuideChartShowCorrections>
        <GuiderName>PHD2_Single</GuiderName>
        <MGENFocalLength>1000</MGENFocalLength>
        <MGENPixelMargin>10</MGENPixelMargin>
        <MaxY>4</MaxY>
        <MetaGuideDitherSettleSeconds>30</MetaGuideDitherSettleSeconds>
        <MetaGuideLockWhenGuiding>false</MetaGuideLockWhenGuiding>
        <MetaGuideMinIntensity>100</MetaGuideMinIntensity>
        <MetaGuidePort>1277</MetaGuidePort>
        <MetaGuideUseIpAddressAny>false</MetaGuideUseIpAddressAny>
        <PHD2GuiderScale>ARCSECONDS</PHD2GuiderScale>
        <PHD2HistorySize>100</PHD2HistorySize>
        <PHD2InstanceNumber>1</PHD2InstanceNumber>
        <PHD2Path>C:\Program Files (x86)\PHDGuiding2\phd2.exe</PHD2Path>
        <PHD2ProfileId i:nil="true"/>
        <PHD2ROIPct>100</PHD2ROIPct>
        <PHD2ServerPort>4400</PHD2ServerPort>
        <PHD2ServerUrl>localhost</PHD2ServerUrl>
        <SettlePixels>1.5</SettlePixels>
        <SettleTime>5</SettleTime>
        <SettleTimeout>40</SettleTimeout>
        <SkyGuardCallbackPort>8000</SkyGuardCallbackPort>
        <SkyGuardPath/>
        <SkyGuardServerPort>18700</SkyGuardServerPort>
        <SkyGuardServerUrl>localhost</SkyGuardServerUrl>
        <SkyGuardTimeLapsChecked>false</SkyGuardTimeLapsChecked>
        <SkyGuardTimeLapsDitherChecked>false</SkyGuardTimeLapsDitherChecked>
        <SkyGuardTimeLapsDithering>60</SkyGuardTimeLapsDithering>
        <SkyGuardTimeLapsGuiding>60</SkyGuardTimeLapsGuiding>
        <SkyGuardTimeOutGuiding>5</SkyGuardTimeOutGuiding>
        <SkyGuardValueMaxDithering>1</SkyGuardValueMaxDithering>
        <SkyGuardValueMaxGuiding>1</SkyGuardValueMaxGuiding>
    </GuiderSettings>
    <Id>f6e49505-b720-479b-9bc7-5b47f9f21d4d</Id>
    <ImageFileSettings i:type="ImageFileSettings">
        <FITSAddFzExtension>true</FITSAddFzExtension>
        <FITSCompressionType>NONE</FITSCompressionType>
        <FITSUseLegacyWriter>true</FITSUseLegacyWriter>
        <FilePath>C:\NINA\Targets\</FilePath>
        <FilePattern> $$TARGETNAME$$\$$CAMERA$$_$$DATEMINUS12$$\$$IMAGETYPE$$\$$TARGETNAME$$_$$DATE$$_$$TIME$$_$$FILTER$$_EXP-$$EXPOSURETIME$$s_$$FRAMENR$$</FilePattern>
        <FilePatternBIAS>
            CALIBRATION\$$CAMERA$$_$$DATEMINUS12$$\BIAS_EXP-$$EXPOSURETIME$$s\BIAS_$$CAMERA$$_$$DATE$$_$$TIME$$_$$FILTER$$_EXP-$$EXPOSURETIME$$s_$$FRAMENR$$
        </FilePatternBIAS>
        <FilePatternDARK>
            CALIBRATION\$$CAMERA$$_$$DATEMINUS12$$\DARK_EXP-$$EXPOSURETIME$$s\DARK_$$CAMERA$$_$$DATE$$_$$TIME$$_$$FILTER$$_EXP-$$EXPOSURETIME$$s_$$FRAMENR$$
        </FilePatternDARK>
        <FilePatternFLAT>
            CALIBRATION\$$CAMERA$$_$$DATEMINUS12$$\FLAT_EXP-$$EXPOSURETIME$$s\FLAT_$$CAMERA$$_$$DATE$$_$$TIME$$_$$FILTER$$_EXP-$$EXPOSURETIME$$s_$$FRAMENR$$
        </FilePatternFLAT>
        <FileType>XISF</FileType>
        <TIFFCompressionType>NONE</TIFFCompressionType>
        <XISFByteShuffling>false</XISFByteShuffling>
        <XISFChecksumType>SHA256</XISFChecksumType>
        <XISFCompressionType>NONE</XISFCompressionType>
    </ImageFileSettings>
    <ImageHistorySettings i:type="ImageHistorySettings">
        <ImageHistoryLeftSelected>HFR</ImageHistoryLeftSelected>
        <ImageHistoryRightSelected>Stars</ImageHistoryRightSelected>
    </ImageHistorySettings>
    <ImageSettings i:type="ImageSettings">
        <AnnotateImage>false</AnnotateImage>
        <AnnotateUnlimitedStars>false</AnnotateUnlimitedStars>
        <AutoStretch>true</AutoStretch>
        <AutoStretchFactor>0.2</AutoStretchFactor>
        <BlackClipping>-2.8</BlackClipping>
        <DebayerImage>true</DebayerImage>
        <DebayeredHFR>true</DebayeredHFR>
        <DetectStars>false</DetectStars>
        <NoiseReduction>Median</NoiseReduction>
        <SharpCapSensorAnalysisFolder i:nil="true"/>
        <StarSensitivity>High</StarSensitivity>
        <UnlinkedStretch>true</UnlinkedStretch>
    </ImageSettings>
    <LastUsed>2024-07-04T14:33:15.634802-06:00</LastUsed>
    <MeridianFlipSettings i:type="MeridianFlipSettings">
        <AutoFocusAfterFlip>true</AutoFocusAfterFlip>
        <MaxMinutesAfterMeridian>10</MaxMinutesAfterMeridian>
        <MinutesAfterMeridian>5</MinutesAfterMeridian>
        <PauseTimeBeforeMeridian>5</PauseTimeBeforeMeridian>
        <Recenter>true</Recenter>
        <RotateImageAfterFlip>true</RotateImageAfterFlip>
        <SettleTime>30</SettleTime>
        <UseSideOfPier>true</UseSideOfPier>
    </MeridianFlipSettings>
    <Name>WO-GT81-0.8_ASI2600_AM5</Name>
    <PlanetariumSettings i:type="PlanetariumSettings">
        <C2AHost>localhost</C2AHost>
        <C2APort>5876</C2APort>
        <CdCHost>localhost</CdCHost>
        <CdCPort>3292</CdCPort>
        <HNSKYHost>localhost</HNSKYHost>
        <HNSKYPort>7700</HNSKYPort>
        <PreferredPlanetarium>STELLARIUM</PreferredPlanetarium>
        <SkytechXHost>localhost</SkytechXHost>
        <SkytechXPort>2055</SkytechXPort>
        <StellariumHost>localhost</StellariumHost>
        <StellariumPort>8090</StellariumPort>
        <TSXHost>localhost</TSXHost>
        <TSXPort>3040</TSXPort>
        <TSXUseSelectedObject>false</TSXUseSelectedObject>
    </PlanetariumSettings>
    <PlateSolveSettings i:type="PlateSolveSettings">
        <ASTAPLocation>C:\Program Files\astap\astap.exe</ASTAPLocation>
        <AspsLocation/>
        <AstrometryAPIKey/>
        <AstrometryURL>http://nova.astrometry.net</AstrometryURL>
        <Binning>1</Binning>
        <BlindFailoverEnabled>true</BlindFailoverEnabled>
        <BlindSolverType>ASTAP</BlindSolverType>
        <CygwinLocation/>
        <DownSampleFactor>0</DownSampleFactor>
        <ExposureTime>5</ExposureTime>
        <Filter i:nil="true" xmlns:a="http://schemas.datacontract.org/2004/07/NINA.Core.Model.Equipment"/>
        <Gain>-1</Gain>
        <MaxObjects>500</MaxObjects>
        <NumberOfAttempts>10</NumberOfAttempts>
        <PS2Location>C:\NINA\PlateSolve2\2.28\PlateSolve2.exe</PS2Location>
        <PS3Location>C:\NINA\PlateSolve3\PlateSolve3.80.exe</PS3Location>
        <PinPointAllSkyApiHost>nova.astrometry.net</PinPointAllSkyApiHost>
        <PinPointAllSkyApiKey/>
        <PinPointCatalogRoot>C:\GSC11\</PinPointCatalogRoot>
        <PinPointCatalogType>ppGSCACT</PinPointCatalogType>
        <PinPointExpansion>40</PinPointExpansion>
        <PinPointMaxMagnitude>20</PinPointMaxMagnitude>
        <PlateSolverType>ASTAP</PlateSolverType>
        <ReattemptDelay>1</ReattemptDelay>
        <Regions>5000</Regions>
        <RotationTolerance>1</RotationTolerance>
        <SearchRadius>30</SearchRadius>
        <SlewToTarget>false</SlewToTarget>
        <Sync>false</Sync>
        <TheSkyXHost>localhost</TheSkyXHost>
        <TheSkyXPort>3040</TheSkyXPort>
        <Threshold>1</Threshold>
    </PlateSolveSettings>
    <PluginSettings i:type="PluginSettings">
        <pluginStorage xmlns:a="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
            <a:KeyValueOfguidArrayOfKeyValueOfstringanyTypeox8ieOcg>
                <a:Key>0f1d10b6-d306-4168-b751-d454cbac9670</a:Key>
                <a:Value>
                    <a:KeyValueOfstringanyType>
                        <a:Key>IntermediateSavePath</a:Key>
                        <a:Value i:type="b:string" xmlns:b="http://www.w3.org/2001/XMLSchema">
                            C:\Users\PrimaLuceLab\AppData\Local\NINA\HocusFocusIntermediate
                        </a:Value>
                    </a:KeyValueOfstringanyType>
                    <a:KeyValueOfstringanyType>
                        <a:Key>NoiseReductionRadius</a:Key>
                        <a:Value i:type="b:int" xmlns:b="http://www.w3.org/2001/XMLSchema">4</a:Value>
                    </a:KeyValueOfstringanyType>
                    <a:KeyValueOfstringanyType>
                        <a:Key>UseAdvanced</a:Key>
                        <a:Value i:type="b:boolean" xmlns:b="http://www.w3.org/2001/XMLSchema">false</a:Value>
                    </a:KeyValueOfstringanyType>
                    <a:KeyValueOfstringanyType>
                        <a:Key>Save</a:Key>
                        <a:Value i:type="b:boolean" xmlns:b="http://www.w3.org/2001/XMLSchema">false</a:Value>
                    </a:KeyValueOfstringanyType>
                    <a:KeyValueOfstringanyType>
                        <a:Key>SavePath</a:Key>
                        <a:Value i:type="b:string" xmlns:b="http://www.w3.org/2001/XMLSchema">C:\NINA\HocusFocus
                        </a:Value>
                    </a:KeyValueOfstringanyType>
                    <a:KeyValueOfstringanyType>
                        <a:Key>ShowAllStars</a:Key>
                        <a:Value i:type="b:boolean" xmlns:b="http://www.w3.org/2001/XMLSchema">false</a:Value>
                    </a:KeyValueOfstringanyType>
                </a:Value>
            </a:KeyValueOfguidArrayOfKeyValueOfstringanyTypeox8ieOcg>
        </pluginStorage>
    </PluginSettings>
    <RotatorSettings i:type="RotatorSettings">
        <Id>Manual Rotator</Id>
        <RangeStartMechanicalPosition>0</RangeStartMechanicalPosition>
        <RangeType>FULL</RangeType>
        <Reverse>true</Reverse>
        <Reverse2>false</Reverse2>
    </RotatorSettings>
    <SafetyMonitorSettings i:type="SafetyMonitorSettings">
        <Id>No_Device</Id>
    </SafetyMonitorSettings>
    <SequenceSettings i:type="SequenceSettings">
        <CloseDomeShutterAtSequenceEnd>true</CloseDomeShutterAtSequenceEnd>
        <CollapseSequencerTemplatesByDefault>false</CollapseSequencerTemplatesByDefault>
        <CoolCameraAtSequenceStart>false</CoolCameraAtSequenceStart>
        <DefaultSequenceFolder>C:\NINA\Sequence\</DefaultSequenceFolder>
        <DisableSimpleSequencer>true</DisableSimpleSequencer>
        <DoMeridianFlip>false</DoMeridianFlip>
        <OpenDomeShutterAtSequenceStart>false</OpenDomeShutterAtSequenceStart>
        <ParkDomeAtSequenceEnd>true</ParkDomeAtSequenceEnd>
        <ParkMountAtSequenceEnd>false</ParkMountAtSequenceEnd>
        <SequenceCompleteCommand i:nil="true"/>
        <SequencerTargetsFolder>C:\NINA\Targets\</SequencerTargetsFolder>
        <SequencerTemplatesFolder>C:\NINA\Template\</SequencerTemplatesFolder>
        <StartupSequenceTemplate/>
        <TemplatePath/>
        <TimeSpanInTicks>0</TimeSpanInTicks>
        <UnparMountAtSequenceStart>true</UnparMountAtSequenceStart>
        <WarmCamAtSequenceEnd>false</WarmCamAtSequenceEnd>
    </SequenceSettings>
    <SnapShotControlSettings i:type="SnapShotControlSettings">
        <ExposureDuration>60</ExposureDuration>
        <Filter xmlns:a="http://schemas.datacontract.org/2004/07/NINA.Core.Model.Equipment">
            <a:FlatWizardFilterSettings>
                <a:Binning>
                    <a:_x>1</a:_x>
                    <a:_y>1</a:_y>
                </a:Binning>
                <a:FlatWizardMode>DYNAMICEXPOSURE</a:FlatWizardMode>
                <a:Gain>-1</a:Gain>
                <a:HistogramMeanTarget>0.5</a:HistogramMeanTarget>
                <a:HistogramTolerance>0.1</a:HistogramTolerance>
                <a:MaxAbsoluteFlatDeviceBrightness>100</a:MaxAbsoluteFlatDeviceBrightness>
                <a:MaxFlatExposureTime>30</a:MaxFlatExposureTime>
                <a:MinAbsoluteFlatDeviceBrightness>0</a:MinAbsoluteFlatDeviceBrightness>
                <a:MinFlatExposureTime>0.01</a:MinFlatExposureTime>
                <a:Offset>-1</a:Offset>
            </a:FlatWizardFilterSettings>
            <a:_autoFocusBinning>
                <a:_x>1</a:_x>
                <a:_y>1</a:_y>
            </a:_autoFocusBinning>
            <a:_autoFocusExposureTime>-1</a:_autoFocusExposureTime>
            <a:_autoFocusFilter>false</a:_autoFocusFilter>
            <a:_autoFocusGain>-1</a:_autoFocusGain>
            <a:_autoFocusOffset>-1</a:_autoFocusOffset>
            <a:_focusOffset>9</a:_focusOffset>
            <a:_name>L-eXtreme</a:_name>
            <a:_position>1</a:_position>
        </Filter>
        <Gain>-1</Gain>
        <Loop>false</Loop>
        <Save>false</Save>
    </SnapShotControlSettings>
    <SwitchSettings i:type="SwitchSettings">
        <Id>ASCOM.EagleSwitch.Switch</Id>
    </SwitchSettings>
    <TelescopeSettings i:type="TelescopeSettings">
        <FocalLength>382</FocalLength>
        <FocalRatio>4.72</FocalRatio>
        <Id>ASCOM.ASIMount.Telescope</Id>
        <MountName>ZWO AM5</MountName>
        <Name>WO GT81 w/ 0.8 Reducer</Name>
        <NoSync>false</NoSync>
        <PrimaryReversed>false</PrimaryReversed>
        <SecondaryReversed>false</SecondaryReversed>
        <SettleTime>5</SettleTime>
        <SnapPortStart>:SNAP1,1#</SnapPortStart>
        <SnapPortStop>SNAP1,0#</SnapPortStop>
        <TelescopeLocationSyncDirection>PROMPT</TelescopeLocationSyncDirection>
        <TimeSync>true</TimeSync>
    </TelescopeSettings>
    <WeatherDataSettings i:type="WeatherDataSettings">
        <Id>ASCOM.ObCo_srv.ObservingConditions</Id>
        <OpenWeatherMapAPIKey/>
        <TheWeatherCompanyAPIKey/>
        <WeatherUndergroundAPIKey/>
        <WeatherUndergroundStation/>
    </WeatherDataSettings>
</Profile>