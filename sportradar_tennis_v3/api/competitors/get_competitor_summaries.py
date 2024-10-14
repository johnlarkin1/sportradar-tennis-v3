from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_competitor_summaries_locale import GetCompetitorSummariesLocale
from ...models.get_competitor_summaries_response_200 import GetCompetitorSummariesResponse200
from ...types import Response


def _get_kwargs(
    locale: GetCompetitorSummariesLocale,
    urn_competitor: str,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/competitors/{urn_competitor}/summaries" + f".{format}",  # Append format to URL
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetCompetitorSummariesResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCompetitorSummariesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetCompetitorSummariesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetCompetitorSummariesLocale,
    urn_competitor: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetCompetitorSummariesResponse200]:
    """list previous and upcoming summaries for a competitor

     List last 30 summaries for a competitor, and all upcoming scheduled sport events.

    Args:
        locale (GetCompetitorSummariesLocale):
        urn_competitor (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompetitorSummariesResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_competitor=urn_competitor, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetCompetitorSummariesLocale,
    urn_competitor: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetCompetitorSummariesResponse200]:
    """list previous and upcoming summaries for a competitor

     List last 30 summaries for a competitor, and all upcoming scheduled sport events.

    Args:
        locale (GetCompetitorSummariesLocale):
        urn_competitor (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompetitorSummariesResponse200
    """

    return sync_detailed(
        locale=locale,
        urn_competitor=urn_competitor,
        client=client,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetCompetitorSummariesLocale,
    urn_competitor: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetCompetitorSummariesResponse200]:
    """list previous and upcoming summaries for a competitor

     List last 30 summaries for a competitor, and all upcoming scheduled sport events.

    Args:
        locale (GetCompetitorSummariesLocale):
        urn_competitor (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompetitorSummariesResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_competitor=urn_competitor, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetCompetitorSummariesLocale,
    urn_competitor: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetCompetitorSummariesResponse200]:
    """list previous and upcoming summaries for a competitor

     List last 30 summaries for a competitor, and all upcoming scheduled sport events.

    Args:
        locale (GetCompetitorSummariesLocale):
        urn_competitor (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompetitorSummariesResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            urn_competitor=urn_competitor,
            client=client,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
