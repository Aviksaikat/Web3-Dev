// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

interface I1inchAggregator {
    function getRate(
        address srcToken,
        address dstToken,
        bool useWrappers
    ) external view returns (uint256);

    function getRateToEth(
        address srcToken,
        bool useWrappers
    ) external view returns (uint256);
}
